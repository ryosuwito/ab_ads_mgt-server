from django.urls import path
from . import views

app_name = 'wilayah'

urlpatterns = [
	path('get_postal_code/<int:kelurahan_code>/', views.get_postal_code, name='get_postal_code'),
    path('get_by_code/<int:kelurahan_code>/', views.get_by_code, name='get_by_code'),
    path('postal_code/<str:postal_code>/', views.get_by_postal_code, name='postal_code'),
    path('provinsi/', views.get_provinsi, name='provinsi'),
    path('kota/<str:nama_provinsi>/', views.get_kota, name='kota'),
    path('kecamatan/<int:pk>/', views.get_kecamatan, name='kecamatan'),
    path('kelurahan/<int:pk>/', views.get_kelurahan, name='kelurahan'),
]                       