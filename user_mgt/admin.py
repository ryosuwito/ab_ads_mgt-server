from django.contrib import admin
from .models import UserRole, Privilege, UserManagement

class UserRoleAdmin(admin.ModelAdmin):
    model = UserRole
  
class PrivilegeAdmin(admin.ModelAdmin):
    model = Privilege
  
class UserManagementAdmin(admin.ModelAdmin):
    model = UserManagement

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Privilege, PrivilegeAdmin)
admin.site.register(UserManagement, UserManagementAdmin)