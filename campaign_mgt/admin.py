from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import StickerType, GpsType, Campaign, VehicleOnCampaign

class StickerTypeAdmin(admin.ModelAdmin):
    model = StickerType

admin.site.register(StickerType, StickerTypeAdmin)

class GpsTypeAdmin(admin.ModelAdmin):
    model = GpsType

admin.site.register(GpsType, GpsTypeAdmin)

class CampaignAdmin(admin.ModelAdmin):
    model = Campaign

admin.site.register(Campaign, CampaignAdmin)

class VehicleOnCampaignAdmin(admin.ModelAdmin):
    model = VehicleOnCampaign

admin.site.register(VehicleOnCampaign, VehicleOnCampaignAdmin)