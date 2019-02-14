from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

app_name = 'vehicle'

urlpatterns = [
    re_path(r'^$', views.AddCarView.as_view(), name='show_all'),
    path('brand/<str:vehicle_type>/', views.GetBrandsView.as_view(), name='get_brands'),
    path('model/<str:vehicle_type>/<str:vehicle_brand>/', views.GetModelsView.as_view(), name='get_models'),
    path('add/', views.AddCarView.as_view(), name='add_new'),
]