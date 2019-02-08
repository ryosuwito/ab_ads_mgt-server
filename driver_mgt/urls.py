from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

app_name = 'driver'

urlpatterns = [
    re_path(r'^$', views.DriverBankView.as_view(), name='driver_profile'),
    path('regis/', views.DriverRegistrationView.as_view(), name='regis_driver'),
    path('bank/', views.DriverBankView.as_view()),
]