from django import forms
from django.contrib.auth.models import User
from .models import Driver
from payment.models import BankAccount

class DriverRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Driver
        exclude = ('user','bank_name', 'bank_branch_name',
            'bank_account_number', 'bank_account_name') 

class DriverBankForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('bank_name', 'bank_branch_name',
            'bank_account_number', 'bank_account_name', 'on_behalf') 