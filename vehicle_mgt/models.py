from django.db import models

from area_db.models import Province, City, Kecamatan, Kelurahan
from driver_mgt.models import Driver

class VehicleColor(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Vehicle Color"
        verbose_name_plural = "Vehicle Colors"
    
    def __str__(self):
        return self.name

class VehicleType(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = "Vehicle Type"
        verbose_name_plural = "Vehicle Types"
    
    def __str__(self):
        return self.name

class VehicleBrand(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Vehicle Brand"
        verbose_name_plural = "Vehicle Brands"
    
    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    name = models.CharField(max_length=30)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.SET_NULL, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Vehicle Model"
        verbose_name_plural = "Vehicle Models"
    
    def __str__(self):
        return self.name

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
    
    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
    
    def __str__(self):
        return self.license_no