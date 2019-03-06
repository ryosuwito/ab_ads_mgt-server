from django.contrib.postgres.fields import JSONField
from django.db import models

class GpsDailyReport(models.Model):
    campaign_name = models.CharField(max_length=255, db_index=True, null=True, default="phd")
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    license_no =  models.CharField(max_length=15, db_index=True, null=True)
    mileage = models.IntegerField(default=0)
    viewer = models.IntegerField(default=0)
    def __str__(self):
        return "%s / %s / %s"%(self.created_date, self.mileage, self.viewer)

class GpsData(models.Model):
    campaign_name = models.CharField(max_length=255, db_index=True, null=True, default="phd")
    license_no = models.CharField(max_length=15, db_index=True)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(max_length=60)
    data = JSONField(null=True)
    def __str__(self):
        return self.license_no

class ImpressionGpsData(models.Model):
    campaign_name = models.CharField(max_length=255, db_index=True, null=True, default="phd")
    postal_code = models.CharField(max_length=50, db_index=True, null=True)
    city = models.CharField(max_length=255, db_index=True, null=True)
    address = models.CharField(max_length=500, db_index=True, null=True)
    license_no = models.CharField(max_length=15, db_index=True)
    latitude = models.CharField(blank=True, null=True, max_length=55)
    longitude = models.CharField(blank=True, null=True, max_length=55)
    status_vehicle = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_engine = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    mileage = models.CharField(blank=True, null=True, max_length=55)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(blank=True, null=True, max_length=60)
    def __str__(self):
        return '%s - %s'%(self.license_no, self.timestamp)


class LastLocation(models.Model):
    campaign_name = models.CharField(max_length=255, db_index=True, null=True, default="phd")
    postal_code = models.CharField(max_length=50, db_index=True, null=True)
    city = models.CharField(max_length=255, db_index=True, null=True)
    address = models.CharField(max_length=500, db_index=True, null=True)
    license_no = models.CharField(max_length=15, db_index=True)
    latitude = models.CharField(blank=True, null=True, max_length=55)
    longitude = models.CharField(blank=True, null=True, max_length=55)
    status_vehicle = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_engine = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    mileage = models.CharField(blank=True, null=True, max_length=55)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(blank=True, null=True, max_length=60)
    data = JSONField(null=True)
    
    def __str__(self):
        return self.license_no

class BlackList(models.Model):
    campaign_name = models.CharField(max_length=255, default='')
    license_no = models.CharField(max_length=15, db_index=True)