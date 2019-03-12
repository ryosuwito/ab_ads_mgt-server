from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from backend import settings
from campaign_mgt.models import GpsType, StickerType, VehicleOnCampaign
import json

class AdvertisementIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')

class AdvertisementAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')

class ReportIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/report.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')
def set_results_status(obj):
	results = {}
	if obj:
		results['status'] = 'OK'
	else:
		results['status'] = 'NO'

	results['results'] = []
	return results

def get_vehicle_on_campaign(request, *args, **kwargs):
    campaign_name = request.GET.get('campaign_name')
    if not campaign_name:
        campaign_name = settings.CAMPAIGN_NAME
    vocs = VehicleOnCampaign.objects.filter(campaign=campaign_name)
    results = set_results_status(vocs)
    data = []
    for l in vocs:
        data.append([l.vehicle_license_no, 
         l.vehicle_domisili, 
         l.vehicle_model,
         l.status,
         l.campaign])
    results['results'].append({'data':data})

    return HttpResponse(json.dumps(results), status=200)
