from tracking_mgt.models import LastLocation
from backend import settings
from .models import GpsData, LastLocation, GpsDailyReport
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
		if current_data > last_data:
			temp_mileage += (current_data - last_data)

	total_mileage = temp_mileage/1000
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
campaign_name = input('Masukan nama campaign:') 
if not campaign_name:
	campaign_name = 'phd'
licenses = [l.license_no for l in LastLocation.objects.filter(campaign_name=campaign_name)]
for l in licenses:
	print(l)
	print(calculate_mileage(l, campaign_name=campaign_name))
