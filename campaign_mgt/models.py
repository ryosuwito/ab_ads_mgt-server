from django.db import models
from advertiser_mgt.models import Advertiser
from agent_mgt.models import Agent
from area_db.models import Province, City, Kecamatan
from vehicle_mgt.models import VehicleModel, VehicleColor, VehicleType, VehicleBrand, Vehicle


class StickerType(models.Model):
    name = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sticker Type"
        verbose_name_plural = "Sticker Types"
    
    def __str__(self):
        return self.name

class GpsType(models.Model):
    name = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "GPS Type"
        verbose_name_plural = "GPS Types"
    
    def __str__(self):
        return self.name

class CampaignInstallation(models.Model):
    photo_sticker_before = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)  
    photo_sticker_after = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    photo_gps_before = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    photo_gps_after = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    photo_odometer = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    photo_form_installation = models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    photo_form_uninstallation= models.ImageField(upload_to = 'campaign/campaign_installation_picture', blank=True)
    gps_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class Campaign(models.Model):
    title = models.CharField(max_length=50)
    gps_type = models.ForeignKey(GpsType, on_delete=models.SET_NULL, null=True)
    sticker_type = models.ForeignKey(StickerType, on_delete=models.SET_NULL, null=True)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.SET_NULL, null=True, blank=True)
    agen = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    timezone = models.CharField(max_length=15, null=True)
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
    terms_and_conditions = models.TextField()
    province = models.ManyToManyField(Province)
    city = models.ManyToManyField(City)
    status = models.CharField(max_length=15, null=True)
    amount_of_vehicle = models.IntegerField()
    installation_address = models.CharField(max_length=255, null=True)
    campaign_picture = models.ImageField(upload_to = 'campaign/campaign_picture', blank=True)
    vehicle_brand = models.ManyToManyField(VehicleBrand)
    vehicle_model = models.ManyToManyField(VehicleModel)
    vehicle_color = models.ManyToManyField(VehicleColor)
    vehicle_type = models.ManyToManyField(VehicleType)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
    
    def __str__(self):
        return self.title

class VehicleOnCampaign(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    gps_installation_schedule = models.DateTimeField(blank=True)
    sticker_installation_schedule = models.DateTimeField(blank=True)
    installation = models.ForeignKey(CampaignInstallation, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Vehicle Campaign"
        verbose_name_plural = "Vehicles on Campaign"
    
    def __str__(self):
        return self.vehicle.license_no