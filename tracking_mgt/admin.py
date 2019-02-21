from django.contrib import admin
from .models import LastLocation, GpsData

class LastLocationAdmin(admin.ModelAdmin):
    model = LastLocation
class GpsDataAdmin(admin.ModelAdmin):
    model = LastLocation
    
admin.site.register(LastLocation, LastLocationAdmin)
admin.site.register(GpsData, GpsDataAdmin)
