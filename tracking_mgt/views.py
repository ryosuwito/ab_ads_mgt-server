from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import model_to_dict
from django.db.models import Sum
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta
from backend import settings
import geopy.distance
from .models import GpsData, LastLocation, GpsDailyReport, DummyGps, LastDummyGps
import requests
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
		campaign_name = settings.CAMPAIGN_NAME
	now = datetime.now()
	date_start = now - timedelta(hours = int(start_date))
	return get_by_license(license_no, start_date=date_start, campaign_name=campaign_name)

def get_before_range(license_no, end_date, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = settings.CAMPAIGN_NAME
	date_end = datetime.strptime(end_date, '%Y-%m-%d')
	return get_by_license(license_no, end_date=date_end, campaign_name=campaign_name)

def get_by_date_range(license_no, start_date, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = settings.CAMPAIGN_NAME
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
		campaign_name = settings.CAMPAIGN_NAME
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
						'idx':i,
						'lat':g.data['latitude'],
						'lng':g.data['longitude']})

	return {
			'license_no':license_no,
			'partition':partition,
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
	included_provinces = ['Sumut', 'Sumatera Utara']
	jabodetabek = ['jakarta', 'depok', 'tangerang', 'bekasi', 'bogor']
	for l in last_locations:
		if l.city == 'JKT':
			l.city = 'Jabodetabek'
		if l.city == 'Jabar':
			l.city = 'Jawa Barat'
		if not l.city in included_cities:
			for p in included_provinces:
				if p in l.address:
					l.city = "Medan"
					break
			if not l.city:
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
		 l.created_date.strftime("%Y-%m-%d %H:%M:%S"),
		 get_driver_viewer(l.license_no)])
	results['results'].append({'cities' : cities})
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

def calculate_mileage(license_no, **kwargs):
	try:
		campaign_name = kwargs['campaign_name']
	except:
		campaign_name = 'marugame'
	if not campaign_name:
		campaign_name = settings.CAMPAIGN_NAME

	data_query = GpsData.objects.filter(campaign_name=campaign_name,license_no=license_no).order_by('created_date').values('data').iterator()
	last_data = 0
	current_data = 0
	temp_mileage = 0
	for i, d in enumerate(data_query):
		start_data = d['data']['mileage']
		current_data = int(start_data)
		diff = current_data - last_data
		if diff > 0:
			print("%s :: %s"%(current_data, diff))
		if current_data > last_data: 
			if (last_data > 0) and (diff < 300):
				temp_mileage += (current_data - last_data)
				print(temp_mileage)
		elif current_data != last_data :
			temp_mileage += current_data
		last_data = current_data
	print('Mileage in Meter %s' % temp_mileage)
	total_mileage = temp_mileage/1000.
	print('Total mileage : %s km'%(total_mileage))
			
	try:
		mileage_report = GpsDailyReport.objects.get(license_no = license_no, 
			campaign_name=campaign_name)
		mileage_report.mileage = total_mileage
		mileage_report.created_date=datetime.now()
		mileage_report.save()
	except:
		GpsDailyReport.objects.create(license_no=license_no,
			mileage=total_mileage,
			campaign_name=campaign_name,
			created_date=datetime.now())
	return total_mileage

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
	included_provinces = ['Sumut', 'Sumatera Utara']
	jabodetabek = ['jakarta', 'depok', 'tangerang', 'bekasi', 'bogor']
	for l in last_locations:
		if l.city == 'JKT':
			l.city = 'Jabodetabek'
		if l.city == 'Jabar':
			l.city = 'Jawa Barat'
		try:
			if not l.city in included_cities:
				for p in included_provinces:
					if p in l.address:
						l.city = "Medan"
						break
				if not l.city:
					l.city = 'Others'
			for j in jabodetabek:
				if j in l.address.lower():
					l.city = 'Jabodetabek'
		except:
			l.city = 'Others'
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

def gps_show_record(request, license_no, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	latest_date = GpsDailyReport.objects.filter(campaign_name=campaign_name,
		license_no=license_no).order_by('created_date').values('created_date').last()

	prev_date = latest_date['created_date'] - timedelta(days=2, hours=23, minutes=59)
	end_date = datetime.strftime(latest_date['created_date'] , '%Y-%m-%d')
	start_date = datetime.strftime(prev_date, '%Y-%m-%d')
	gps_data = get_by_date_range(license_no, start_date,
		end_date = end_date)
	results = set_results_status(gps_data)
	results['results'].append(gps_data)
	return HttpResponse(json.dumps(results), status=200)

def gps_all_record(request, **kwargs):
	campaign_name = settings.CAMPAIGN_NAME
	licenses = LastLocation.objects.all().values('license_no','created_date')\
		.order_by('-created_date').distinct()
	res = []
	for l in licenses:
		res.append({'created_date': datetime.strftime(l['created_date'] , '%Y-%m-%d'),
			'license_no':l['license_no']})
	results = set_results_status(res)
	results['results'].append({'data': res})
	return HttpResponse(json.dumps(results), status=200)

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
	date_list = GpsDailyReport.objects.values('viewer','mileage').filter(campaign_name=campaign_name).annotate(date=TruncDate('created_date')).order_by('created_date').iterator()
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

@csrf_exempt
def save_gps_data(request, license_no, *args, **kwargs):
	created_date = datetime.now()
	lat = request.GET.get('lat',"")
	lng = request.GET.get('lng',"")
	lastlat = request.GET.get('lastlat',"")
	lastlng = request.GET.get('lastlng',"")
	campaign = request.GET.get('cmp',"")
	campaign = campaign.lower()
	campaign = "".join([c for c in campaign if c.isalnum()])
	license_no = license_no.replace(" ","").lower()
	license_no = "".join([l for l in license_no if l.isalnum()])
	if campaign != settings.CAMPAIGN_NAME and campaign != "":
		return HttpResponseRedirect("http://"+campaign+".abplusscar.com/gps/save/"+license_no+"/?lat="+lat+"&lng="+lng+"&cmp="+campaign)
	try:
		last_gps = LastDummyGps.objects.get(license_no=license_no)
	except:
		last_gps = ""

	if not last_gps:
		last_gps = LastDummyGps.objects.create(license_no=license_no, mileage=0,
			campaign_name = campaign, created_date=created_date, latitude=lat, longitude=lng)
	else:
		if not lastlat:
			lastlat = last_gps.latitude
		if not lastlng:
			lastlng = last_gps.longitude


	if(lastlat and lastlng):
		coor1 = (float(lat), float(lng))
		coor2 = (float(lastlat), float(lastlng))
		distance = repr(int(geopy.distance.vincenty(coor1, coor2).km * 1000 * 0.89))
	else:
		distance = 0
	#distance = 0;

	if lat and lng:
		dummy = DummyGps.objects.create(license_no=license_no, mileage=distance,
			campaign_name = campaign, created_date=created_date, latitude=lat, longitude=lng)
		last_gps.latitude = lat
		last_gps.longitude = lng
		last_gps.created_date = created_date
		last_gps.save()
		last_location, stat = LastLocation.objects.get_or_create(
				license_no = license_no,
				campaign_name = campaign
			)
		if last_location:
			last_location.data = {"latitude":lat,"longitude":lng, "mileage":distance, 
				"timestamp":datetime.now().timestamp() , "timeformat":created_date.strftime('%Y-%m-%d %H:%M:%S')}
			last_location.timestamp = datetime.now().timestamp()
			last_location.created_date = created_date.strftime('%Y-%m-%d %H:%M:%S')
			last_location.latitude = lat
			last_location.longitude = lng
			last_location.status_vehicle = "ACTIVE"
			last_location.status_engine = "ON"
			last_location.mileage = distance
			last_location.address = "None"
			city = "Other"

			last_location.city = city
			postcode = ''
			last_location.postal_code = postcode
			last_location.save()

		gps, stat = GpsData.objects.get_or_create(
				license_no = license_no,
				timestamp = datetime.now().timestamp()
			)
		#print(gps.timestamp)
		if gps:
			gps.data = {"latitude":lat,"longitude":lng, "mileage":distance,
				"timestamp":datetime.now().timestamp() , "timeformat":created_date.strftime('%Y-%m-%d %H:%M:%S')}
			gps.campaign_name = campaign
			gps.created_date = created_date.strftime('%Y-%m-%d %H:%M:%S')
			gps.save()
		return HttpResponse("OK")
	else:
		return HttpResponse("NOT OK")
