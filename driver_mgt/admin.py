from django.contrib import admin
from .models import Driver

class DriverAdmin(admin.ModelAdmin):
    model = Driver

admin.site.register(Driver, DriverAdmin)