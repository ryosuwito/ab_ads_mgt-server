from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from datetime import datetime, timedelta
from .models import GpsData, LastLocation
import json

def get_all_licences():
	return list(set([l['license_no'] for l in LastLocation.objects.all().values('license_no').iterator()]))

def get_by_range(license_no, start_date, **kwargs):
	now = datetime.now()
	date_start = now - timedelta(hours = int(start_date))
	return get_by_license(license_no, start_date=date_start)

def get_before_range(license_no, end_date, **kwargs):
	date_end = datetime.strptime(end_date, '%Y-%m-%d')
	return get_by_license(license_no, end_date=date_end)

def get_by_date_range(license_no, start_date, **kwargs):
	try:
		end_date = kwargs['end_date']
	except Exception as e:
		print(e)
		end_date = ''
		date_end = ''

	date_start = datetime.strptime(start_date, '%Y-%m-%d')
	if end_date:
		date_end = datetime.strptime(end_date, '%Y-%m-%d')
	return get_by_license(license_no, start_date=date_start, end_date=date_end)

def get_by_license(license_no, **kwargs):
	try:
		start_date = kwargs['start_date']
	except Exception as e:
		print(e)
		start_date = ''

	try:
		end_date = kwargs['end_date']
	except Exception as e:
		print(e)
		end_date = ''

	if end_date:
		if not start_date:
			gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__lte=end_date)
		else:
			gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date, created_date__lte=end_date)
	elif start_date:
		gps = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=start_date)
	else:
		gps = GpsData.objects.filter(license_no=license_no.upper())

	data = [{'lat':gps[0].data['latitude'],
			'lng':gps[0].data['longitude']}]
			
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
	end_date = request.GET.get('end_date')
	if not license_no:
		licenses = get_all_licences()
		results = set_results_status(licenses)
		if end_date:
			if start_date:
				for license in licenses:
					results['results'].append(get_by_date_range(license, start_date, end_date))
			else:
				for license in licenses:
					results['results'].append(get_by_date_before(license, end_date))
		elif start_date:
			for license in licenses:
				results['results'].append(get_by_date_range(license, start_date))
		else:
			for license in licenses:
				results['results'].append(get_by_license(license))
			
	else:
		results = set_results_status(license_no)
		if end_date:
			if start_date:
				results['results'].append(get_by_date_range(license_no, start_date, end_date))
			else:
				results['results'].append(get_by_date_before(license_no, end_date))
		elif start_date:
			results['results'].append(get_by_date_range(license_no, start_date))
		else:
			results['results'].append(get_by_license(license_no))
				
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