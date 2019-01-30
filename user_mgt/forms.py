from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username/ Phone/ Email :', max_length=150)
    attrs = {
        "type": "password"
    }
    password = forms.CharField(label='Password :', widget=forms.PasswordInput(attrs=attrs))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'input-text'
        self.fields['password'].widget.attrs['style'] = 'width:100%'
        self.fields['username'].widget.attrs['class'] = 'input-text'
        self.fields['username'].widget.attrs['style'] = 'width:100%'