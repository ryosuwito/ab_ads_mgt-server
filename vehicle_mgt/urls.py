from django.urls import path, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'vehicle'

urlpatterns = [
    re_path(r'^$', login_required(views.AddCarView.as_view()), name='show_all'),
    path('brand/<str:vehicle_type>/', login_required(views.GetBrandsView.as_view()), name='get_brands'),
    path('model/<str:vehicle_type>/<str:vehicle_brand>/', login_required(views.GetModelsView.as_view()), name='get_models'),
    path('add/', login_required(views.AddCarView.as_view()), name='add_new'),
]