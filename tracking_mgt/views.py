from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from django.db.models import Sum
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta
from backend import settings
from campaign_mgt.models import VehicleOnCampaign
from .models import GpsData, LastLocation, GpsDailyReport
import json

def get_all_licences(**kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = settings.CAMPAIGN_NAME
	if not campaign_name:
		return [l['license_no'] for l in LastLocation.objects.all().values('license_no').iterator()]
	else:
		return [l['license_no'] for l in LastLocation.objects.filter(campaign_name=campaign_name).values('license_no').iterator()]


def get_by_range(license_no, start_date, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = ''
	now = datetime.now()
	date_start = now - timedelta(hours = int(start_date))
	return get_by_license(license_no, start_date=date_start, campaign_name=campaign_name)

def get_before_range(license_no, end_date, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = ''
	date_end = datetime.strptime(end_date, '%Y-%m-%d')
	return get_by_license(license_no, end_date=date_end, campaign_name=campaign_name)

def get_by_date_range(license_no, start_date, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = ''
	try:
		end_date = kwargs['end_date']
	except Exception as e:
		print(e)
		end_date = ''
		date_end = ''

	date_start = datetime.strptime(start_date, '%Y-%m-%d')
	if end_date:
		date_end = datetime.strptime(end_date, '%Y-%m-%d')
	return get_by_license(license_no, campaign_name=campaign_name, start_date=date_start, end_date=date_end)

def get_by_license(license_no, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = ''
	try:
		start_date = kwargs['start_date']
	except Exception as e:
		print(e)
		start_date = ''

	try:
		partition = int(kwargs['partition'])
	except Exception as e:
		print(e)
		partition = 1

	try:
		end_date = kwargs['end_date']
	except Exception as e:
		print(e)
		end_date = ''

	if not campaign_name:
		if end_date:
			if not start_date:
				gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__lte=end_date).order_by('-timestamp').iterator()
			else:
				gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date, created_date__lte=end_date).order_by('-timestamp').iterator()
		elif start_date:
			gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date).order_by('-timestamp').iterator()
		else:
			gps = GpsData.objects.filter(license_no=license_no.upper()).order_by('-timestamp').iterator()
	else:
		if end_date:
			if not start_date:
				gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__lte=end_date).order_by('-timestamp').iterator()
			else:
				gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__gte=start_date, created_date__lte=end_date).order_by('-timestamp').iterator()
		elif start_date:
			gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__gte=start_date).order_by('-timestamp').iterator()
		else:
			gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper()).order_by('-timestamp').iterator()
	
	data = []

	if gps:
		for i, g in enumerate(gps):
			if i%partition == 0 or i==0:
				data.append({
						'partition':partition,
						'idx':i,
						'lat':g.data['latitude'],
						'lng':g.data['longitude']})

	return {
			'license_no':license_no,
			# 'created_date':g.created_date,
			# 'timestamp':g.timestamp,
			'data':data
		}

def set_results_status(obj):
	results = {}
	if obj:
		results['status'] = 'OK'
	else:
		results['status'] = 'NO'

	results['results'] = []
	return results

def gps_show_all(request, *args, **kwargs):
	license_no = request.GET.get('license_no')
	campaign_name = request.GET.get('campaign_name')
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')
	partition = request.GET.get('partition')
	if not license_no:
		licenses = get_all_licences()
		results = set_results_status(licenses)
		if end_date:
			if start_date:
				for license in licenses:
					results['results'].append(get_by_date_range(license, start_date, end_date, campaign_name=campaign_name))
			else:
				for license in licenses:
					results['results'].append(get_by_date_before(license, end_date, campaign_name=campaign_name))
		elif start_date:
			for license in licenses:
				results['results'].append(get_by_date_range(license, start_date, campaign_name=campaign_name))
		else:
			for license in licenses:
				results['results'].append(get_by_license(license, partition=partition, campaign_name=campaign_name))
			
	else:
		results = set_results_status(license_no)
		if end_date:
			if start_date:
				results['results'].append(get_by_date_range(license_no, start_date, end_date, campaign_name=campaign_name))
			else:
				results['results'].append(get_by_date_before(license_no, end_date, campaign_name=campaign_name))
		elif start_date:
			results['results'].append(get_by_date_range(license_no, start_date, campaign_name=campaign_name))
		else:
			results['results'].append(get_by_license(license_no, partition=partition, campaign_name=campaign_name))
				
	return HttpResponse(json.dumps(results), status=200)

def gps_show_all_license(request, *args, **kwargs):
	campaign_name = request.GET.get('campaign_name')
	licenses = get_all_licences(campaign_name=campaign_name)
	results = set_results_status(licenses)

	results['results'] = licenses
	return HttpResponse(json.dumps(results), status=200)

def gps_get_all_last_locations(request, *args, **kwargs):
	campaign_name = request.GET.get('campaign_name')
	if not campaign_name:
		campaign_name = settings.CAMPAIGN_NAME
	licenses = LastLocation.objects.filter(campaign_name=campaign_name)
	results = set_results_status(licenses)
	last_locations = [l for l  in licenses]
	cities = {}
	included_cities = ['Jabodetabek', 'Bali', 'Medan', 'Jawa Barat']
	jabodetabek = ['jakarta', 'depok', 'tangerang', 'bekasi', 'bogor']
	for l in last_locations:
		if l.city == 'JKT':
			l.city = 'Jabodetabek'
		if not l.city in included_cities:
			l.city = 'Others'
		for j in jabodetabek:
			if j in l.address.lower():
				l.city = 'Jabodetabek'
		try:
			city = cities[l.city]
			cities[l.city] += 1
		except Exception as e:
			print(e)
			cities[l.city] = 1
	cities = {key: value for (key, value) in sorted(cities.items())}
	data = []
	for l in licenses:
		data.append([l.license_no, 
		 l.latitude, 
		 l.longitude,
		 l.status_vehicle,
		 l.status_engine,
		 get_driver_mileage(l.license_no, campaign_name=campaign_name),
		 l.address if l.address else "-",
		 l.city if l.city else "-",
		 l.created_date.strftime("%Y-%m-%d %H:%M:%S")])
	results['results'].append({'cities' : cities})
	results['results'].append({'data':data})

	return HttpResponse(json.dumps(results), status=200)
# def gps_show_by_license(request, license_no, *args, **kwargs):
# 	results = set_results_status(license_no)
# 	results['results'].append(get_by_license(license_no))
# 	return HttpResponse(json.dumps(results), status=200)


def get_driver_last_location(request, license_no):
	campaign_name = request.GET.get('campaign_name')
	if not campaign_name:
		campaign_name = settings.CAMPAIGN_NAME
	licenses = LastLocation.objects.filter(campaign_name=campaign_name,
		license_no = license_no)[:1]
	results = set_results_status(licenses)
	last_locations = [l for l  in licenses]
	city = ""
	included_cities = ['Jabodetabek', 'Bali', 'Medan', 'Jawa Barat']
	jabodetabek = ['jakarta', 'depok', 'tangerang', 'bekasi', 'bogor']
	for l in last_locations:
		if l.city == 'JKT':
			l.city = 'Jabodetabek'
		if not l.city in included_cities:
			l.city = 'Others'
		for j in jabodetabek:
			if j in l.address.lower():
				l.city = 'Jabodetabek'
		city = l.city
	data = []
	for l in licenses:
		data = [l.license_no, 
		 l.latitude, 
		 l.longitude,
		 l.status_vehicle,
		 l.status_engine,
		 get_driver_mileage(l.license_no, campaign_name=campaign_name),
		 l.address if l.address else "-",
		 l.city if l.city else "-",
		 l.created_date.strftime("%Y-%m-%d %H:%M:%S",
		 get_driver_viewer(l.license_no))]
	results['results'].append({'city' : city})
	results['results'].append({'data':data})

	return HttpResponse(json.dumps(results), status=200)

def get_driver_mileage(license_no, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	try:
		total_mileage= GpsDailyReport.objects.filter(license_no = license_no, 
			campaign_name=campaign_name).aggregate(Sum('mileage'))['mileage__sum']	
	except:
		total_mileage = 0
	if total_mileage:
		return str(int(total_mileage))
	else:
		return "0"

def get_driver_viewer(license_no, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	try:
		total_viewer = GpsDailyReport.objects.filter(license_no = license_no, 
			campaign_name=campaign_name).aggregate(Sum('viewer'))['viewer__sum']	
	except:
		total_viewer = 0
	if total_viewer:
		return str(int(total_viewer))
	else:
		return "0"

def get_daily_report(request, *args, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	date_list = GpsDailyReport.objects.values('viewer','mileage')\
		.filter(campaign_name=campaign_name).annotate(date=TruncDate('created_date')).order_by('created_date').iterator()
	datelist = {}
	results = set_results_status(date_list)
	for d in date_list:
		try:
			datelist[str(d['date'])]['viewer'] += int(d['viewer'])
			datelist[str(d['date'])]['mileage'] += int(d['mileage'])
			print(int(d['mileage']))
		except Exception as e:
			datelist[str(d['date'])] = { 'mileage' : int(d['mileage']), 'viewer' : int(d['viewer'])}
	results['results'].append({'datelist' : datelist})
	return HttpResponse(json.dumps(results), status=200)

def get_report_by_date(request, date_string, *args, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	date = datetime.strptime(date_string, "%Y-%m-%d")
	date_end = date + timedelta(days=1)
	date_list = GpsDailyReport.objects.values('license_no','viewer','mileage')\
		.filter(campaign_name=campaign_name, created_date__gte=date, created_date__lte=date_end).iterator()
	datelist = []
	results = set_results_status(date_list)
	for d in date_list:
		try:
			unit_model = VehicleOnCampaign.objects.get(vehicle_license_no=d['license_no']).vehicle_model
		except:
			unit_model = "mobil"
		datelist.append({
			'license_no':d['license_no'],
			'unit':unit_model,
			'viewer':d['viewer'],
			'mileage':int(d['mileage'])
			})
	results['results'].append({'reportlist' : datelist})
	return HttpResponse(json.dumps(results), status=200)