from django.shortcuts import render
from django.views import View
from .forms import AddCarForm

class AddCarView(View):
    form = AddCarForm()
    form_messages = ''
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/add_vehicle.html',
            {'form': self.form,
            'form_messages': self.form_messages})