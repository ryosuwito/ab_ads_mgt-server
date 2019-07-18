from tracking_mgt.models import *
from backend import settings

def find_last_location():
        all_data = []
        with open("driver_data.csv") as f:
                for line in f:
                        data = line.rstrip().replace(" ","").split(";")
                        all_data.append(data)
        # licenses = GpsData.objects.all().values("license_no").distinct()
        # licenses_list = [l["license_no"] for l in licenses]
        for l in all_data :
                try:
                        last_location = LastLocation.objects.filter(license_no=l[0], campaign_name=settings.CAMPAIGN_NAME)[0]
                        last_location.city = all_data[l[1]]
                        last_location.save()
                        print("%s -- OK "%(l))
                except Exception as e:
                        print("%s -- NOT OK "%(l))
                        print(e)
                        pass

find_last_location()