from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from datetime import datetime, timedelta
from backend import settings
from .models import GpsData, LastLocation, GpsDailyReport
import json

def get_all_licences(**kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = ''
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
		partition = 60

	try:
		end_date = kwargs['end_date']
	except Exception as e:
		print(e)
		end_date = ''

	if not campaign_name:
		if end_date:
			if not start_date:
				gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__lte=end_date).order_by('-timestamp')
			else:
				gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date, created_date__lte=end_date).order_by('-timestamp')
		elif start_date:
			gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date).order_by('-timestamp')
		else:
			gps = GpsData.objects.filter(license_no=license_no.upper()).order_by('-timestamp')
	else:
		if end_date:
			if not start_date:
				gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__lte=end_date).order_by('-timestamp')
			else:
				gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__gte=start_date, created_date__lte=end_date).order_by('-timestamp')
		elif start_date:
			gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper(), created_date__gte=start_date).order_by('-timestamp')
		else:
			gps = GpsData.objects.filter(campaign_name=campaign_name, license_no=license_no.upper()).order_by('-timestamp')
	
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
		licenses = LastLocation.objects.all()
	else:
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
	results['results'].append({'cities' : cities})
	for l in licenses:
		results['results'].append({'data' : 
			[l.license_no, 
			 l.latitude, 
			 l.longitude,
			 l.status_vehicle,
			 l.status_engine,
			 calculate_driver_mileage(l.license_no, campaign_name=settings.CAMPAIGN_NAME),
			 l.address if l.address else "-",
			 l.city if l.city else "-",
			 l.created_date.strftime("%Y-%m-%d %H:%M:%S")]})
	return HttpResponse(json.dumps(results), status=200)
# def gps_show_by_license(request, license_no, *args, **kwargs):
# 	results = set_results_status(license_no)
# 	results['results'].append(get_by_license(license_no))
# 	return HttpResponse(json.dumps(results), status=200)

def calculate_driver_mileage(license_no, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = 'marugame'
	try:
		mileage_report = GpsDailyReport.objects.get(license_no = license_no, 
			campaign_name=campaign_name)
		total_mileage = mileage_report.mileage
	except:
		total_mileage = 0
	return total_mileage

# def calculate_driver_mileage(license_no, **kwargs):
# 	try:
# 		campaign_name = kwargs['campaign_name']
# 	except:
# 		campaign_name = 'marugame'
# 	try:
# 		mileage_report = GpsDailyReport.objects.get(license_no = license_no, 
# 			campaign_name=campaign_name)
# 		total_mileage = mileage_report.mileage
# 	except:
# 		if not campaign_name:
# 			start_data = GpsData.objects.filter(license_no=license_no).order_by('timestamp').values('data').first()
# 			end_data = GpsData.objects.filter(license_no=license_no).order_by('timestamp').values('data').last()
# 		else:
# 			start_data = GpsData.objects.filter(campaign_name=campaign_name,license_no=license_no).order_by('timestamp').values('data').first()
# 			end_data = GpsData.objects.filter(campaign_name=campaign_name,license_no=license_no).order_by('timestamp').values('data').last()
# 		if start_data and end_data:
# 			print('Starting mileage : %s'%start_data['data']['mileage'])
# 			print('Ending mileage : %s'%end_data['data']['mileage'])
# 			total_mileage = (int(end_data['data']['mileage'])-int(start_data['data']['mileage']))/1000
# 			print('Total mileage : %s'%(total_mileage))
# 			GpsDailyReport.objects.create(license_no=license_no,
# 				mileage=total_mileage,
# 				campaign_name=campaign_name,
# 				created_date=datetime.now())
# 		else:
# 			total_mileage = 'Data Kurang'
# 	return total_mileage