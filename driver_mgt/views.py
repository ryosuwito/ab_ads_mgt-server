from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.views import View
from area_db.models import Province,City,Kecamatan,Kelurahan
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from .forms import DriverRegistrationForm,DriverBankForm
from .models import Driver
import secrets

class DriverRegistrationView(View):
    form = DriverRegistrationForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        provinces = Province.objects.all()
        return render(request, 'backend/registration/driver_index.html',
            {'form': self.form,
            'provinces': provinces,
            'token': get_token(request),
            'form_messages': self.form_messages})
            
    def post(self, request, *args, **kwargs):
        provinces = Province.objects.all()
        self.form = DriverRegistrationForm(request.POST, request.FILES)
        if self.form.is_valid(): 
            data = self.form.cleaned_data
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
        return render(request, 'backend/registration/driver_index.html',
            {'form': self.form,
            'provinces': provinces,
            'token': get_token(request),
            'form_messages': self.form_messages})

@csrf_exempt
def driver_self_regis_view(request, *args, **kwargs):
    form = DriverRegistrationForm()
    form_messages = ''
    if request.method == "GET":
        return HttpResponse("bad method")
            
    elif request.method == "POST":
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
                return HttpResponseRedirect("http://abplusscar.com/success.html")
            else:
                return HttpResponseRedirect("http://abplusscar.com/failed.html")
        return HttpResponseRedirect("http://abplusscar.com/success.html")

class DriverBankView(View):
    form = DriverBankForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'driver_mgt/regis.html',
            {'form': self.form,
            'form_messages': self.form_messages})            
    def post(self, request, *args, **kwargs):
        self.form = DriverBankForm(request.POST)
        if self.form.is_valid():
            return HttpResponse('OK GAN')
        return render(request, 'driver_mgt/regis.html',
            {'form': self.form,
            'form_messages': self.form_messages})

class DriverMasterDataView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/masterdata.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/masterdata.html')


@csrf_exempt
def driver_login_view(request, *args, **kwargs):
    plat = request.POST.get("plat", "")
    campaign = request.POST.get("campaign", "")
    token = secrets.token_urlsafe(25)
    return JsonResponse({"plat":plat, "campaign":campaign, "token":token})


@csrf_exempt
def driver_upload_bukti_tayang(request, license_no, *args, **kwargs):
    files = request.FILES
    token = secrets.token_urlsafe(25)
    return JsonResponse({"plat":license_no, "files":len(files), "token":token})