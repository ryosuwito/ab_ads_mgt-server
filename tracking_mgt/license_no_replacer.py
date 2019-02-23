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
		location.save
		print("Loc : %s of %s : %s"%(idx, data_len, l))

	idx = 0
	locations = GpsData.objects.all().iterator()
	data_len = GpsData.objects.all().count()
	print(locations)
	for location in locations:
		idx+=1
		l = location.license_no.replace(" ","").upper()
		location.license_no = l
		location.save
		print("Gps : %s of %s : %s"%(idx, data_len, l))