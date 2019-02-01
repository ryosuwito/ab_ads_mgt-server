from django import forms
from django.contrib.auth.models import User
from .models import Driver

class DriverRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Driver
        exclude = ('user','bank_name', 'bank_branch_name',
            'bank_account_number', 'bank_account_name') 

class DriverBankForm(forms.ModelForm):
    on_behalf = forms.CharField()
    class Meta:
        model = Driver
        fields = ('bank_name', 'bank_branch_name',
            'bank_account_number', 'bank_account_name') 