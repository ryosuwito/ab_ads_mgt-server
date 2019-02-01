from django.contrib.postgres.fields import JSONField
from django.db import models

class GpsData(models.Model):
    license_no = models.CharField(max_length=15, db_index=True)
    crated_date = models.DateTimeField(auto_now=False, db_index=True, blank=True, null=True)
    timestamp = models.CharField(max_length=60, db_index=True)
    data = JSONField()
    """ 
    gps_state = models.CharField(max_length=30, null=True, blank=True)
    gps = models.IntegerField()
    time = models.IntegerField()
    username = models.CharField(max_length=30)
    time_format = models.CharField(max_length=30)
    terminal = models.CharField(max_length=15)
    owner_telp = models.CharField(max_length=20, null=True, blank=True)
    owner_name = models.CharField(max_length=50, null=True, blank=True)
    gps_type = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    speed = models.IntegerField()
    direction = models.IntegerField()
    mileage = models.IntegerField()
    alarm_state = models.IntegerField(null=True, blank=True)
    car_state = models.IntegerField(null=True, blank=True)
    icon_id = models.IntegerField(null=True, blank=True)
    gsm = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    status_engine = models.CharField(max_length=15, null=True, blank=True)
    exp_date = models.DateField(auto_now=False, null=True, blank=True)
    status_exp = models.CharField(max_length=15, null=True, blank=True)
    vehicle_state = models.CharField(max_length=15, null=True, blank=True)
    vehicle_type = models.CharField(max_length=15, null=True, blank=True)
    kelurahan = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=30)
    kota = models.CharField(max_length=30)
    provisi = models.CharField(max_length=30)
    user_login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    column = models.IntegerField()
    """
    
    def __str__(self):
        return self.license_no