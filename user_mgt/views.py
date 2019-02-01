from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
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
        return HttpResponseRedirect(reverse('membership:login'))   