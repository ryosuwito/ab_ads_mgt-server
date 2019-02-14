from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View
from area_db.models import Province,City,Kecamatan,Kelurahan
from django.middleware.csrf import get_token
from .forms import DriverRegistrationForm,DriverBankForm
from .models import Driver

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
            user = User.objects.create_user(username=username,
                email=email,
                password=password)
            if user:
                try:
                    driver = Driver.objects.create(
                          full_name = full_name,
                          user = user,
                          ktp_photo = ktp_photo,
                          mobile_phone=mobile_phone,
                          address=address,
                          province = Province.objects.get(pk=provinsi),
                          city = City.objects.get(pk=kota),
                          kecamatan = Kecamatan.objects.get(pk=kecamatan),
                          kelurahan = Kelurahan.objects.get(pk=kelurahan)
                        )
                except Exception as e:
                    print(e)
                    return HttpResponse('NOT OK GAN')
                return HttpResponseRedirect(reverse('vehicle:add_new'))
            else:
                return HttpResponse('NOT OK GAN')
        return render(request, 'backend/registration/driver_index.html',
            {'form': self.form,
            'provinces': provinces,
            'token': get_token(request),
            'form_messages': self.form_messages})


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
