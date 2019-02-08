from django import forms
from django.contrib.auth.models import User
from .models import Driver
from payment.models import BankAccount

class DriverRegistrationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    full_name = forms.CharField()
    address = forms.CharField()
    email =  forms.EmailField()
    mobile_phone = forms.CharField()
    ktp_photo = forms.ImageField(allow_empty_file=False)

    def __init__(self, *args, **kwargs):
        super(DriverRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['style'] = 'width:100%'
        self.fields['password'].widget.attrs['type'] = '********'
        self.fields['password'].widget.attrs['required'] = 'required'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = '********'
        self.fields['confirm_password'].widget.attrs['style'] = 'width:100%'
        self.fields['confirm_password'].widget.attrs['type'] = 'password'
        self.fields['confirm_password'].widget.attrs['required'] = 'required'
        self.fields['confirm_password'].widget.attrs['rdata-validate-linked'] = 'id_password'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['style'] = 'width:100%'
        self.fields['full_name'].widget.attrs['type'] = 'text'
        self.fields['full_name'].widget.attrs['required'] = 'required'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['style'] = 'width:100%'
        self.fields['address'].widget.attrs['type'] = 'text'
        self.fields['address'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['style'] = 'width:100%'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['data-parsley-trigger'] = 'change'
        self.fields['mobile_phone'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_phone'].widget.attrs['style'] = 'width:100%'
        self.fields['mobile_phone'].widget.attrs['type'] = 'number'
        self.fields['mobile_phone'].widget.attrs['required'] = 'required'
        self.fields['ktp_photo'].widget.attrs['class'] = 'form-control'
        self.fields['ktp_photo'].widget.attrs['style'] = 'width:100%'
        self.fields['ktp_photo'].widget.attrs['required'] = 'required'
        self.fields['ktp_photo'].widget.attrs['onchange'] = 'previewImage();'



class DriverBankForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('bank_name', 'bank_branch_name',
            'bank_account_number', 'bank_account_name', 'on_behalf') 