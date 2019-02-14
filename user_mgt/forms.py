from django import forms
from django.contrib.auth.models import User
from .models import UserRole

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username/ Phone/ Email :', max_length=150)
    password = forms.CharField(label='Password :', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['style'] = 'width:100%'
        self.fields['password'].widget.attrs['type'] = 'password'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'width:100%'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

class AddBackOfficeForm(forms.Form):
    OPTIONS = UserRole.objects.filter(is_archived=False)
    full_name = forms.CharField(label='Nama')
    email =  forms.EmailField()
    mobile_phone = forms.CharField()
    profile_picture = forms.ImageField(allow_empty_file=False)
    password = forms.CharField(label='Password :', widget=forms.PasswordInput())
    role = forms.ModelMultipleChoiceField(OPTIONS, initial='')
    is_active = forms.BooleanField(initial=True)

    def __init__(self, *args, **kwargs):
        super(AddBackOfficeForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['style'] = 'width:100%'
        self.fields['password'].widget.attrs['type'] = 'password'
        self.fields['password'].widget.attrs['required'] = 'required'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['style'] = 'width:100%'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['full_name'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['style'] = 'width:100%'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['mobile_phone'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_phone'].widget.attrs['style'] = 'width:100%'
        self.fields['mobile_phone'].widget.attrs['type'] = 'number'
        self.fields['mobile_phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['mobile_phone'].widget.attrs['required'] = 'required'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['profile_picture'].widget.attrs['style'] = 'width:100%'
        self.fields['profile_picture'].widget.attrs['required'] = 'required'     
        self.fields['profile_picture'].widget.attrs['onchange'] = 'previewImage3(this.id);'
        self.fields['is_active'].widget.attrs['required'] = 'required'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['style'] = 'width:100%'
        self.fields['role'].widget.attrs['required'] = 'required'

class AddUserRoleForm(forms.Form):
    role_name = forms.CharField(label='Nama')
    description =  forms.CharField()
    is_active = forms.BooleanField()
    def __init__(self, *args, **kwargs):
        super(AddUserRoleForm, self).__init__(*args, **kwargs)
        self.fields['role_name'].widget.attrs['class'] = 'form-control'
        self.fields['role_name'].widget.attrs['style'] = 'width:100%'
        self.fields['role_name'].widget.attrs['placeholder'] = 'Role Name'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['style'] = 'width:100%'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['is_active'].widget.attrs['class'] = 'flat'