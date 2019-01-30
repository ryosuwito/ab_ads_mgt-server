from django.db import models
from area_db.models import Province, City, Kecamatan
from vehicle_mgt.models import VehicleModel, VehicleColor, Vehicle


class StickerType(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Sticker Type"
        verbose_name_plural = "Sticker Types"
    
    def __str__(self):
        return self.name

class GpsType(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = "GPS Type"
        verbose_name_plural = "GPS Types"
    
    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    gps_type = models.ForeignKey(GpsType, on_delete=models.SET_NULL, null=True)
    sticker_type = models.ForeignKey(StickerType, on_delete=models.SET_NULL, null=True)
    #todo::foreignkey ke agen dan advertiser
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    campaign_start_date = models.DateTimeField(blank=True)
    campaign_end_date = models.DateTimeField(blank=True)
    publish_start_date = models.DateTimeField(blank=True)
    publish_end_date = models.DateTimeField(blank=True)
    installation_start_date = models.DateTimeField(blank=True)
    installation_end_date = models.DateTimeField(blank=True)
    minimum_milage = models.IntegerField()
    minimum_payment = models.IntegerField()
    special_campaign_point = models.IntegerField()
    terms_and_conditions = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15)
    no_of_vehicle = models.IntegerField()
    installation_address = models.CharField(max_length=255)
    campaign_picture = models.ImageField(upload_to = 'campaign/campaign_picture', blank=True)
    vehicle_models = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    vehicle_color = models.ForeignKey(VehicleColor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
    
    def __str__(self):
        return self.name

class VehicleOnCampaign(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    gps_installation_schedule = models.DateTimeField(blank=True)
    sticker_installation_schedule = models.DateTimeField(blank=True)
    status = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Vehicle Campaign"
        verbose_name_plural = "Vehicles on Campaign"
    
    def __str__(self):
        return self.vehicle.license_no