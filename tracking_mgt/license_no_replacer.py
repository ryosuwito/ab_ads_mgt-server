from tracking_mgt.models import GpsData, LastLocation

def replace():
	idx = 0
	locations = LastLocation.objects.all().iterator()
	data_len = LastLocation.objects.all().count()
	print(locations)
	for location in locations:
		idx+=1
		l = location.license_no.replace(" ","").upper()
		location.license_no = l
		location.save()
		print("Loc : %s of %s : %s"%(idx, data_len, l))

	idx = 0
	locations = GpsData.objects.all().iterator()
	data_len = GpsData.objects.all().count()
	print(locations)
	for location in locations:
		idx+=1
		l = location.license_no.replace(" ","").upper()
		location.license_no = l
		location.save()
		print("Gps : %s of %s : %s"%(idx, data_len, l))

def find_duplicate():
	data = GpsData.objects.all().exclude(campaign_name='marugame').exclude(campaign_name='phd').iterator()
	for idx, d in enumerate(data):
		try:
			ob = GpsData.objects.get(license_no=d.license_no, 
				timestamp=d.timestamp)
			if 'phd' in ob.campaign_name:
				c_name = 'phd'
			elif 'marugame' in ob.campaign_name:
				c_name = 'marugame'
			else:
				print(ob.campaign_name)
				print('+++++++++++++++++++++++++++')
				continue
			try:
				ex = GpsData.objects.get(license_no=d.license_no, 
				timestamp=d.timestamp, campaign_name = c_name)
				print('DUPLICATE FOUND !!!')
				print(' - '.join([ex.license_no, ob.license_no]))
				print(' - '.join([ex.timestamp, ob.timestamp]))
				print(ob.data)
				print(ex.data)
				ob.delete()
			except:
				print('EX FOUND - DUPLICATE NOT FOUND')
				ob.campaign_name = c_name
		except:
			print('DUPLICATE NOT FOUND')
			ob.campaign_name = c_name