from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View
from .forms import DriverRegistrationForm,DriverBankForm

class DriverRegistrationView(View):
    form = DriverRegistrationForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/driver_index.html',
            {'form': self.form,
            'form_messages': self.form_messages})
            
    def post(self, request, *args, **kwargs):
        self.form = DriverRegistrationForm(request.POST, request.FILES)
        if self.form.is_valid(): 
            data = self.form.cleaned_data
            full_name = data.get('full_name')
            email = data.get('email')
            password = data.get('password')
            username = full_name.replace(' ','_').lower()
            user = User.objects.create_user(username=username,
                email=email,
                password=password)
            if user:
                return HttpResponseRedirect(reverse('vehicle:add_new'))
            else:
                return HttpResponse('NOT OK GAN')
        return render(request, 'backend/registration/driver_index.html',
            {'form': self.form,
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
