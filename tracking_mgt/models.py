from django.contrib.postgres.fields import JSONField
from django.db import models

class GpsDailyReport(models.Model):
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    mileage = models.IntegerField()
    viewer = models.IntegerField()
    def __str__(self):
        return "%s / %s / %s"%(self.created_date, self.mileage, self.viewer)

class GpsData(models.Model):
    license_no = models.CharField(max_length=15, db_index=True)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(max_length=60, db_index=True)
    data = JSONField(null=True)
    def __str__(self):
        return self.license_no

class ImpressionGpsData(models.Model):
    postal_code = models.CharField(max_length=50, db_index=True, null=True)
    city = models.CharField(max_length=255, db_index=True, null=True)
    address = models.CharField(max_length=500, db_index=True, null=True)
    license_no = models.CharField(max_length=15, db_index=True)
    latitude = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    longitude = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_vehicle = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_engine = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    mileage = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(blank=True, null=True, max_length=60, db_index=True)
    def __str__(self):
        return '%s - %s'%(self.license_no, self.timestamp)


class LastLocation(models.Model):
    postal_code = models.CharField(max_length=50, db_index=True, null=True)
    city = models.CharField(max_length=255, db_index=True, null=True)
    address = models.CharField(max_length=500, db_index=True, null=True)
    license_no = models.CharField(max_length=15, db_index=True)
    latitude = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    longitude = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_vehicle = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    status_engine = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    mileage = models.CharField(blank=True, null=True, max_length=55, db_index=True)
    created_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(blank=True, null=True, max_length=60, db_index=True)
    data = JSONField(null=True)
    
    def __str__(self):
        return self.license_no