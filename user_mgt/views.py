from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.utils.crypto import get_random_string
from django.views import View
from user_mgt.models import Privilege, UserRole, UserManagement
from .forms import UserLoginForm, AddBackOfficeForm, AddUserRoleForm


class BackOfficeIndexView(View):
    form =  AddBackOfficeForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        user_managements = UserManagement.objects.filter(is_archived=False)
        return render(request, 'backend/registration/back_office_index.html',
            {'form': self.form,
            'form_messages': self.form_messages,
            'user_managements':user_managements})            
    def post(self, request, *args, **kwargs):
        user_managements = UserManagement.objects.filter(is_archived=False)
        self.form = AddBackOfficeForm(request.POST, request.FILES)
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
                user_management = UserManagement.objects.create(
                    user=user,
                    full_name=full_name,
                    is_active=data.get('is_active'),
                    profile_picture=data.get('profile_picture'),
                    mobile_phone=data.get('mobile_phone'))
            else:
                self.form_messages = 'Gagal Membuat akun back office'
            if user_management:
                for role in data.get('role'):
                    try:
                        user_management.role.add(UserRole.objects.get(name=role))
                    except Exception as e:
                        print(e)
                        print('Tidak ada role dengan nama {}'.format(role))
                user_management.save()
                self.form_messages = 'Sukses membuat akun back office'
            else:
                self.form_messages = 'Gagal Membuat user management back office'

        else:
            self.form_messages = 'Field error, periksa ulang form back office'
        return render(request, 'backend/registration/back_office_index.html',
            {'form': self.form,
            'form_messages': self.form_messages,
            'user_managements':user_managements}) 

class RoleRemoveView(View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')
        if pk:
            try:
                user_role = UserRole.objects.get(pk=pk)
                user_role.is_archived = True
                user_role.save()
            except:
                pass
        return HttpResponseRedirect(reverse('role_management'))

class RoleEditView(View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')
        if pk:
            try:
                user_role = UserRole.objects.get(pk=pk)
                if user_role.is_active:
                    user_role.is_active = False
                else:
                    user_role.is_active = True
                user_role.save()
            except:
                pass
        return HttpResponseRedirect(reverse('role_management'))

class RoleView(View):
    form =  AddUserRoleForm()
    form_messages = ''
    user_role = ''
    def get(self, request, *args, **kwargs):
        query =  request.GET.get('query')
        if not query:
            self.user_role = UserRole.objects.filter(is_archived=False)
        else:
            self.user_role = UserRole.objects.filter(is_archived=False, 
                name__contains=query)
        return render(request, 'backend/role.html',
            {'user_role':self.user_role,
            'form': self.form,
            'form_messages': self.form_messages})            
    def post(self, request, *args, **kwargs):

        self.user_role = UserRole.objects.filter(is_archived=False)
        self.form = AddUserRoleForm(request.POST)
        if self.form.is_valid():
            data = self.form.cleaned_data
            user_role = UserRole.objects.create(
                    name= data.get('role_name'),
                    description= data.get('description'),
                    is_active= data.get('is_active')
                )
            privileges = []
            post_data =[p for p in request.POST]
            for key in post_data:
                if not key == 'csrfmiddlewaretoken'\
                    and not key == 'role_name'\
                    and not key == 'description'\
                    and not key == 'is_active':
                    data = request.POST.get(key)
                    if data == 'on':
                        obj, stat = Privilege.objects.get_or_create(name=key)
                        privileges.append(obj)
            if privileges:
                for p in privileges:
                    user_role.privilege.add(p)

        return render(request, 'backend/role.html',
            {'user_role':self.user_role,
            'form': self.form,
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