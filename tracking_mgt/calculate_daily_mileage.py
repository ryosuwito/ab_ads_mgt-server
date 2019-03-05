from backend import settings
from .views import calculate_mileage
from .models import GpsData, LastLocation, GpsDailyReport

campaign_name = input('Masukan nama campaign:') 
if not campaign_name:
	campaign_name = 'phd'
licenses = [l.license_no for l in LastLocation.objects.filter(campaign_name=campaign_name)]
for l in licenses:
	print(l)
	print(calculate_mileage(l, campaign_name=campaign_name))
