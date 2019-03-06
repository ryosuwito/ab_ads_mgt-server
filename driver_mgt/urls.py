from django.urls import path, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'driver'

urlpatterns = [
    re_path(r'^$', login_required(views.DriverBankView.as_view()), name='driver_profile'),
    path('master/', login_required(views.DriverMasterDataView.as_view()), name='masterdata_driver'),
    path('regis/', login_required(views.DriverRegistrationView.as_view()), name='regis_driver'),
    path('bank/', login_required(views.DriverBankView.as_view())),
]