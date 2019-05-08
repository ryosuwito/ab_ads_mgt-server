from django.shortcuts import render
from django.views import View
from backend import settings

class ShowBrandPostView(View):
    web_settings = {'url': settings.MAIN_URL}
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/brandlist.html',
            {'settings': self.web_settings})            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/brandlist.html',
            {'settings': self.web_settings})
