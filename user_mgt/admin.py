from django.contrib import admin
from .models import UserType, Privilege, UserManagement

class UserTypeAdmin(admin.ModelAdmin):
    model = UserType
  
class PrivilegeAdmin(admin.ModelAdmin):
    model = Privilege
  
class UserManagementAdmin(admin.ModelAdmin):
    model = UserManagement

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Privilege, PrivilegeAdmin)
admin.site.register(UserManagement, UserManagementAdmin)