from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import UserLoginForm, AddBackOfficeForm

class AddBackOfficeView(View):
    form =  AddBackOfficeForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'driver_mgt/regis.html',
            {'form': self.form,
            'form_messages': self.form_messages})            
    def post(self, request, *args, **kwargs):
        self.form = AddBackOfficeForm(request.POST)
        if self.form.is_valid():
            return HttpResponse('OK GAN')
        return render(request, 'driver_mgt/regis.html',
            {'form': self.form,
            'form_messages': self.form_messages})

class DashboardView(View):
    form =  AddBackOfficeForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html',
            {'form': self.form,
            'form_messages': self.form_messages})            
    def post(self, request, *args, **kwargs):
        self.form = AddBackOfficeForm(request.POST)
        if self.form.is_valid():
            return HttpResponse('OK GAN')
        return render(request, 'backend/main_dashboard.html',
            {'form': self.form,
            'form_messages': self.form_messages})

class Login(View):    
    form = UserLoginForm()
    form_messages = ''
    next = False
    def get(self, request, *args, **kwargs):
        self.next = request.GET.get('next') if request.GET.get('next') else False
        return render(request, 'backend/login.html',
            {'next': self.next,
            'form': self.form,
            'form_messages': self.form_messages})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        self.form = UserLoginForm(request.POST)
        self.next = request.GET.get('next') if request.GET.get('next') else False
        if self.form.is_valid():
            data = self.form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username,
                password=password)
            if not user :
                try:
                    user = User.objects.get(email=username)
                except:
                    user = ''
                if user:
                    user = authenticate(username=user.username,
                        password=password)

            if user:
                login(request, user)
                if self.next:
                    return HttpResponseRedirect(self.next)

                return HttpResponseRedirect(reverse('dashboard'))

        self.form_messages='Login Failed. Wrong username or password'
        return render(request, 'backend/login.html',
            {'next': self.next,
            'form': self.form,
            'form_messages': self.form_messages})

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/login')   

class ForgotPasswordView(View):
    """docstring for ForgotPasswordView"""
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/forgot.html')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        if not email:
            return render(request, 'backend/forgot.html')
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print(e)
            user = ''

        if user:
            amount = 50
            random_number = ''
            random_number = get_random_string(amount, 
                allowed_chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_')
            return render(request, 'backend/reset_success.html', {'random_number':random_number})
        else:
            return render(request, 'backend/reset_failed.html')