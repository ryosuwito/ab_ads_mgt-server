from django.contrib import admin
from .models import VehicleModel, VehicleColor, VehicleType, VehicleBrand, VehicleYear, Vehicle

class VehicleYearAdmin(admin.ModelAdmin):
    model = VehicleYear

class VehicleColorAdmin(admin.ModelAdmin):
    model = VehicleColor

class VehicleTypeAdmin(admin.ModelAdmin):
    model = VehicleType

class VehicleBrandAdmin(admin.ModelAdmin):
    model = VehicleBrand

class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle

class VehicleModelAdmin(admin.ModelAdmin):
    model = VehicleModel

admin.site.register(VehicleYear, VehicleYearAdmin)
admin.site.register(VehicleColor, VehicleColorAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(VehicleBrand, VehicleBrandAdmin)
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(Vehicle, VehicleAdmin)