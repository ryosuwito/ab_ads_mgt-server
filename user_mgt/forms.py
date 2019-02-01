from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username/ Phone/ Email :', max_length=150)
    password = forms.CharField(label='Password :', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['style'] = 'width:100%'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'width:100%'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

class AddBackOfficeForm(forms.Form):
    OPTIONS = (("1", "One"), ("2", "two"),)
    name = forms.CharField(label='Nama')
    email =  forms.EmailField()
    mobile = forms.CharField()
    profile_picture = forms.ImageField(allow_empty_file=False)
    password = forms.CharField(label='Password :', widget=forms.PasswordInput())
    role = forms.ChoiceField(choices=OPTIONS)
    active = forms.BooleanField(initial=True)