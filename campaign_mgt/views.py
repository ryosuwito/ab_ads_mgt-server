from django.shortcuts import render
from django.views import View

class AdvertisementIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/advertisement.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/advertisement.html')

class ReportIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/report.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')
