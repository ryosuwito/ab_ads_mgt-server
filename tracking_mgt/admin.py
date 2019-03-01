from django.contrib import admin
from .models import LastLocation, GpsData, GpsDailyReport

class LastLocationAdmin(admin.ModelAdmin):
    model = LastLocation
class GpsDataAdmin(admin.ModelAdmin):
    model = LastLocation
class GpsDailyReportAdmin(admin.ModelAdmin):
    model = GpsDailyReport
    
admin.site.register(LastLocation, LastLocationAdmin)
admin.site.register(GpsDailyReport, GpsDailyReportAdmin)
admin.site.register(GpsData, GpsDataAdmin)
