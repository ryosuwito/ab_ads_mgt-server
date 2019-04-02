from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
	path('driver/<str:license_no>/', views.get_driver_last_location),
	path('lastlocations/', views.gps_get_all_last_locations),
	path('dailyreport/', views.get_daily_report),
	path('datereport/<str:date_string>/', views.get_report_by_date),
	path('license/', views.gps_show_all_license),
	path('', views.gps_show_all, name='show_all'),
]