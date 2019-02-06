from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

app_name = 'vehicle'

urlpatterns = [
    re_path(r'^$', views.AddCarView.as_view(), name='show_all'),
    path('add/', views.AddCarView.as_view()),
]