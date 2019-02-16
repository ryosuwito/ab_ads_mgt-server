from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from datetime import datetime, timedelta
from .models import GpsData
import json

def get_all_licences():
	return list(set([l['license_no'] for l in GpsData.objects.all().values('license_no')]))

def get_by_range(license_no, start_date, **kwargs):
	now = datetime.now()
	date_start = now - timedelta(hours = int(start_date))
	return get_by_license(license_no, start_date=date_start)

def get_by_license(license_no, **kwargs):
	try:
		start_date = kwargs['start_date']
		print(start_date)
	except Exception as e:
		start_date = ''

	if start_date:
		gps = GpsData.objects.filter(license_no=license_no, created_date__gte=start_date)
	else:
		gps = GpsData.objects.filter(license_no=license_no)

	data = ['new google.maps.LatLng(%s, %s)'%(g.data['latitude'], g.data['longitude']) for g in gps[:500]]
			# [{'lat':g.data['latitude'],
			# 'lng':g.data['longitude'],} for g in gps]
			#'mileage':g.data['mileage']} for g in gps]
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
	start_date = request.GET.get('start_date')
	if not license_no:
		licenses = get_all_licences()
		results = set_results_status(licenses)
		if not start_date:
			for license in licenses:
				results['results'].append(get_by_license(license))
		else:
			for license in licenses:
				results['results'].append(get_by_range(license, start_date))
	else:
		results = set_results_status(license_no)
		if not start_date:
			results['results'].append(get_by_license(license_no))
		else:
			results['results'].append(get_by_range(license_no, start_date))

		
	return HttpResponse(json.dumps(results), status=200)

def gps_show_all_license(request, *args, **kwargs):
	licenses = get_all_licences()
	results = set_results_status(licenses)

	results['results'] = licenses
	return HttpResponse(json.dumps(results), status=200)

# def gps_show_by_license(request, license_no, *args, **kwargs):
# 	results = set_results_status(license_no)
# 	results['results'].append(get_by_license(license_no))
# 	return HttpResponse(json.dumps(results), status=200)