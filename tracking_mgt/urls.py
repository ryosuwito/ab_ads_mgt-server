from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
	path('lastlocations/', views.gps_get_all_last_locations),
    path('license/', views.gps_show_all_license),
    path('', views.gps_show_all, name='show_all'),
]