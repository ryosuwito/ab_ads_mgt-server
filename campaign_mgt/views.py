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
        web_settings = {'url': settings.MAIN_URL}   
        return render(request, 'backend/registration/report.html',
            {'settings': web_settings})            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')

class ReportIndexView(View):
    def get(self, request, *args, **kwargs):
        web_settings = {'url': settings.MAIN_URL, 'CAMPAIGN_NAME':settings.CAMPAIGN_NAME}   
        return render(request, 'backend/registration/photo_report.html',
            {'settings': web_settings})            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')

class RecordIndexView(View):
    def get(self, request, *args, **kwargs):
        web_settings = {'url': settings.MAIN_URL}   
        return render(request, 'backend/registration/record.html',
            {'settings': web_settings})            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')

def advertisement_self_add_view(request, *args, **kwargs):
    form = DriverRegistrationForm()
    form_messages = ''
    if request.method == "GET":
        return HttpResponse("Bad Method")
    if request.method == "POST":
        provinces = Province.objects.all()
        form = DriverRegistrationForm(request.POST, request.FILES)
        if form.is_valid(): 
            data = form.cleaned_data
            provinsi = request.POST.get('provinsi')
            kota = request.POST.get('kota')
            kecamatan = request.POST.get('kecamatan')
            kelurahan = request.POST.get('kelurahan')
            full_name = data.get('full_name')
            email = data.get('email')
            password = data.get('password')
            ktp_photo = data.get('ktp_photo')
            mobile_phone = data.get('mobile_phone')
            address = data.get('address')
            username = full_name.replace(' ','_').lower()
            old_user = User.objects.filter(username=username)
            if old_user:
                username = '%s%s'%(username,len(old_user)+1)
            user = User.objects.create_user(username=username,
                password=password)
            if user:
                driver = Driver.objects.create(
                      full_name = full_name,
                      user = user,
                      ktp_photo = ktp_photo,
                      mobile_phone=mobile_phone,
                      address=address,
                      province = Province.objects.get(pk=provinsi),
                    )
                if kota and not kota == '...' and kota != '0':
                    city = City.objects.get(pk=kota)
                    driver.city = city
                if kecamatan and not kecamatan == '...' and kecamatan != '0':
                    kecamatan = Kecamatan.objects.get(pk=kecamatan)
                    driver.kecamatan = kecamatan
                if kelurahan and not kelurahan == '...' and kelurahan != '0':
                    kelurahan = Kelurahan.objects.get(pk=kelurahan)
                    driver.kelurahan = kelurahan
                driver.user.email = email
                driver.save()
                driver.user.save()
                return HttpResponseRedirect(reverse('vehicle:add_new'))
            else:
                return HttpResponse('NOT OK GAN')
        return HttpResponse("Form Invalid")
        return HttpResponse("Form Invalid") 

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
