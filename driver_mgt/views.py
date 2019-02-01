from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import DriverRegistrationForm,DriverBankForm

class DriverRegistrationView(View):
    form = DriverRegistrationForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'driver_mgt/regis.html',
            {'form': self.form,
            'form_messages': self.form_messages})
            
    def post(self, request, *args, **kwargs):
        self.form = DriverRegistrationForm(request.POST)
        if self.form.is_valid():
            return HttpResponse('OK GAN')
        return render(request, 'driver_mgt/regis.html',
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
