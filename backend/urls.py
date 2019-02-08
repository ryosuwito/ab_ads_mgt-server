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
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from user_mgt import views as user_view

urlpatterns = [
    re_path('^$', login_required(user_view.DashboardView.as_view()), name='dashboard'),
    path('admin/', admin.site.urls),
    path('driver/', include('driver_mgt.urls')),
    path('vehicle/', include('vehicle_mgt.urls')),
    path('user/', include('user_mgt.urls')),
    path('login/', user_view.Login.as_view(), name='login'),
    path('logout/', user_view.Logout.as_view(), name='logout'),    
    path('bo/', user_view.BackOfficeIndexView.as_view(), name='regis_bo'),
    path('bo/edit/', user_view.BackOfficeIndexView.as_view(), name='bo_edit'),
    path('role/', user_view.RoleView.as_view(), name='role_management'),  
    path('role/remove/', user_view.RoleRemoveView.as_view(), name='role_remove'),  
    path('role/edit/', user_view.RoleEditView.as_view(), name='role_edit'),  
    path('gps/', include('tracking_mgt.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
