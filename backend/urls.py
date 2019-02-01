"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from driver_mgt.views import DriverRegistrationView, DriverBankView
from vehicle_mgt.views import AddCarView
from django.conf import settings
from django.conf.urls.static import static
from user_mgt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/regis/', DriverRegistrationView.as_view()),
    path('driver/bank/', DriverBankView.as_view()),
    path('vehicle/add', AddCarView.as_view()),
    path('user/', include('user_mgt.urls')),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)