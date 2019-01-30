from django.db import models

from driver_mgt.models import Driver
from area_db.models import Province, City, Kecamatan, Kelurahan

class VehicleColor(models.Model):
    name = models.CharField(max_length=15)

class VehicleType(models.Model):
    name = models.CharField(max_length=15)

class VehicleBrand(models.Model):
    name = models.CharField(max_length=30)

class VehicleModel(models.Model):
    name = models.CharField(max_length=30)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.SET_NULL, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)

class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    license_no = models.CharField(max_length=15)
    vehicle_year = models.CharField(max_length=4)
    vehicle_color = models.ForeignKey(VehicleColor, on_delete=models.SET_NULL, null=True)
    vehicle_province = models.ForeignKey(Province, on_delete=models.SET_NULL, db_index=True, null=True)
    vehicle_city = models.ForeignKey(City, on_delete=models.SET_NULL, db_index=True, null=True)
    vehicle_kecamatan = models.ForeignKey(Kecamatan, on_delete=models.SET_NULL, db_index=True, null=True)
    vehicle_used_for = models.CharField(max_length=30)
    daily_main_route = models.CharField(max_length=255)
    stnk_photo = models.ImageField(upload_to = 'vehicle/stnk_photo', blank=True)
    front_side_photo = models.ImageField(upload_to = 'vehicle/front_side_photo', blank=True)
    status = models.CharField(max_length=15)