from django.contrib import admin
from .models import VehicleColor, VehicleType, VehicleBrand, Vehicle

class VehicleColorAdmin(admin.ModelAdmin):
    model = VehicleColor

class VehicleTypeAdmin(admin.ModelAdmin):
    model = VehicleType

class VehicleBrandAdmin(admin.ModelAdmin):
    model = VehicleBrand

class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle

admin.site.register(VehicleColor, VehicleColorAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(VehicleBrand, VehicleBrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)