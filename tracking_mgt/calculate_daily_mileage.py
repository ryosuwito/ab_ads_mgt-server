# from backend import settings
# from tracking_mgt.views import calculate_mileage
# from tracking_mgt.models import GpsData, LastLocation, GpsDailyReport
# import time

# campaign_name = input('Masukan nama campaign:') 
# if not campaign_name:
# 	campaign_name = 'phd'

# while true :
# 	licenses = [l.license_no for l in LastLocation.objects.filter(campaign_name=campaign_name)]
# 	for l in licenses:
# 		print(l)
# 		print(calculate_mileage(l, campaign_name=campaign_name))
# 	time.sleep(1*60*60)
