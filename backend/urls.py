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
from agent_mgt import views as agent_view
import area_db.urls as wilayah
 
urlpatterns = [
    re_path('^$', login_required(user_view.DashboardView.as_view()), name='dashboard'),
    path('admin/', admin.site.urls),
    path('campaign/', include('campaign_mgt.urls')),
    path('branding/', login_required(agent_view.ShowBrandPostView.as_view()), name='branding_position'),
    path('driver/', include('driver_mgt.urls')),
    path('payment/', include('payment.urls')),
    path('vehicle/', include('vehicle_mgt.urls')),
    path('wilayah/', include(wilayah, namespace='wilayah_backend')),
    path('user/', include('user_mgt.urls')),
    path('login/', user_view.Login.as_view(), name='login'),
    path('logout/', user_view.Logout.as_view(), name='logout'),    
    path('bo/password/', login_required(user_view.BackOfficeChangePasswordView.as_view()), name='bo_change_password'),
    path('bo/profile/', login_required(user_view.BackOfficeProfileView.as_view()), name='profile_bo'),
    path('bo/regis/', login_required(user_view.BackOfficeIndexView.as_view()), name='regis_bo'),
    path('bo/edit/', login_required(user_view.BackOfficeEditView.as_view()), name='bo_edit'),
    path('role/', login_required(user_view.RoleView.as_view()), name='role_management'),  
    path('role/remove/', login_required(user_view.RoleRemoveView.as_view()), name='role_remove'),  
    path('role/edit/', login_required(user_view.RoleEditView.as_view()), name='role_edit'),  
    path('gps/', include('tracking_mgt.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
