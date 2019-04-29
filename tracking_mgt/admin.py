from django.contrib import admin
from .models import LastLocation, GpsData, GpsDailyReport, DummyGps

class LastLocationAdmin(admin.ModelAdmin):
    model = LastLocation
class GpsDataAdmin(admin.ModelAdmin):
    model = LastLocation
class GpsDailyReportAdmin(admin.ModelAdmin):
    model = GpsDailyReport
class DummyGpsAdmin(admin.ModelAdmin):
    model = DummyGps

    
admin.site.register(LastLocation, LastLocationAdmin)
admin.site.register(GpsDailyReport, GpsDailyReportAdmin)
admin.site.register(GpsData, GpsDataAdmin)
admin.site.register(DummyGps, DummyGpsAdmin)
