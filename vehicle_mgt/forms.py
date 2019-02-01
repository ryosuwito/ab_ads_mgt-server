from django import forms
from django.contrib.auth.models import User
from .models import Vehicle

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Vehicle 
        exclude = ('status',)