from django.urls import path, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'campaign'

urlpatterns = [
    re_path(r'^$', login_required(views.AdvertisementIndexView.as_view()), name='show_all'),
    path('add/', login_required(views.AdvertisementAddView.as_view()), name='add'),
    path('self-add/', login_required(views.advertisement_self_add_view), name='add'),
    path('report/', login_required(views.ReportIndexView.as_view()), name="report"),
    path('photo_report/', login_required(views.PhotoReportIndexView.as_view()), name="photo_report"),
    path('record/', login_required(views.RecordIndexView.as_view()), name="record"),
    path('voc/', views.get_vehicle_on_campaign, name="get_voc"),
]