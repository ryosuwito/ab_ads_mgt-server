from tracking_mgt.models import GpsData, LastLocation, GpsDailyReport
from campaign_mgt.models import VehicleOnCampaign
from django.db.models.functions import TruncDate
from django.db.models import Count
from backend.settings import CAMPAIGN_NAME
import datetime, json, random
import requests

def location_handler(lat,lang):
    base_url="https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?"+\
    "prox=%s,%s,50&mode=retrieveAddresses&maxresults=1&"%(lat,lang)+\
    "gen=9&app_id=PWyLdl8ASf3FPZNpW78C&app_code=jjTXqyys9sDuSaBLfFn_7g"
    #print(base_url)
    profile = {}
    vehicles = {}
        #print(url)
    response = requests.get(base_url).text
    #print(response)
    try:
        data = json.loads(response)
        #print(data)
    except Exception as e:
        print(e)
        data={'response':'NO'}
    try:
    	return data['Response']['View'][0]['Result'][0]['Location']['Address']
    except:
    	return ""

def get_date_list():
	data = GpsData.objects.values('license_no').annotate(date=TruncDate('created_date')).annotate(c=Count('license_no')).order_by().iterator()
	date_list = {}
	for d in data:
	     try:
	         date_list[d['date'].strftime("%Y-%m-%d")] += 1
	     except:
	         date_list[d['date'].strftime("%Y-%m-%d")] = 0
	return date_list

def get_gps_by_date(date, license_no):
	datestart =datetime.datetime.strptime(date, "%Y-%m-%d")
	dateend = datestart + datetime.timedelta(hours=23, minutes=59)
	dData = GpsData.objects.filter(license_no=license_no.upper(), created_date__gte=datestart, created_date__lte=dateend).values('data').order_by('created_date').iterator()
	return dData

def calculate_mileage(data_query):
	last_data = 0
	current_data = 0
	temp_mileage = 0
	for i, d in enumerate(data_query):
		start_data = d['data']['mileage']
		current_data = int(start_data)
		print(current_data)
		#print(current_data)
		if ((current_data - last_data) > 100) and ((current_data - last_data) < 5):
			pass
		elif current_data < 270 and current_data > 27:
			temp_mileage += current_data
		last_data = current_data
	print('Mileage in Meter %s' % temp_mileage)
	total_mileage = temp_mileage/1000
	print('Total mileage : %s km'%(total_mileage))

	return total_mileage

date_list = get_date_list()
objects_list = {}
print(date_list)
licenses = list(set([l['license_no'] for l in GpsData.objects.values('license_no').iterator()]))
with open('workfile', 'w') as f:
	for l in licenses:
		input_l = l
		l = l.upper().replace(" ","")
		try:
			print(l)
			vehicle = VehicleOnCampaign.objects.get(vehicle_license_no=l)
			domisili = vehicle.vehicle_domisili
		except Exception as e:
			print(e)
			domisili = "none"

		for key, value in date_list.items():
			dData = get_gps_by_date(key, input_l)
			print(l)
			tmp = []
			for d in dData:
				#print(d['data'])
				#t_data.append(d['data'])
				tmp.append(d)
			mileage = calculate_mileage(tmp)

			if mileage > 1:
				l = l.upper().replace(" ","")
				try:
					obj = objects_list[key]
				except:
					objects_list[key] = {}
					obj = objects_list[key]

				print(key)
				try:
					t_data = obj[l]
				except:
					obj[l] = {}
					t_data = obj[l]
				t_data['mileage']=int(mileage)
				sample = random.choice(tmp)
				result_sample = location_handler(sample['data']['latitude'],
					sample['data']['longitude'])
				#t_data['sample']=sample
				if result_sample:
					try:
						t_data['city']=result_sample['City']
					except:
						t_data['city']="others"
				t_data['domisili']=domisili
	f.write(str(json.dumps(objects_list,sort_keys=True, indent=4)))

base_impression = {
	'Jakarta' : 300,
	'Tangerang' : 250,
	'Bogor' : 200,
	'Depok' : 250,
	'Bekasi' : 200

}
with open('monthly_dump.csv', 'w') as f:
	idx = 1
	for key, value in objects_list.items():
		d = key.split("-")
		for k, v in value.items():
			for ky, vl in base_impression.items():
				try:
					if ky in v['city']:
						impression = random.randint(55,vl)
						break
					else:
						impression = 150
				except:
					impression = 150
					break

			date_string = "/".join([d[1],d[2],d[0]])
			try:
				mileage_report = GpsDailyReport.objects.get(license_no = k.upper(), 
					campaign_name=CAMPAIGN_NAME,
					created_date = datetime.datetime.strptime(date_string, "%m/%d/%Y")
				)
				mileage_report.mileage = v['mileage']
				mileage_report.viewer = int(v['mileage'] * impression)
				mileage_report.save()
			except:
				GpsDailyReport.objects.create(license_no=k.upper(),
					mileage=v['mileage'],
					viewer=int(v['mileage'] * impression),
					campaign_name=CAMPAIGN_NAME,
					created_date=datetime.datetime.strptime(date_string, "%m/%d/%Y"))
			try:
				v_city = v['city']
			except:
				v['city'] = 'others'
			f.writelines("{};{};{};{};{};{};{}\n".format(idx,
				date_string,
				k,
				v['domisili'],
				v['city'],
				v['mileage'],
				int(v['mileage'] * impression)
				))
			idx += 1
