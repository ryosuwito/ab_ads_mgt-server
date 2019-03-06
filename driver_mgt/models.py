from django.db import models

from django.contrib.auth.models import User
from area_db.models import Province, City, Kecamatan, Kelurahan
from payment.models import BankAccount

class Driver(models.Model):
    full_name = models.CharField(max_length=255, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True)
    mobile_phone = models.CharField(max_length=20, default='', blank=True)
    address = models.CharField(max_length=255, blank=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, db_index=True, null=True)
    city = models.ForeignKey(City, blank=True, on_delete=models.SET_NULL, db_index=True, null=True)
    kecamatan = models.ForeignKey(Kecamatan, blank=True, on_delete=models.SET_NULL, db_index=True, null=True)
    kelurahan = models.ForeignKey(Kelurahan, blank=True, on_delete=models.SET_NULL, db_index=True, null=True)
    ktp_photo = models.ImageField(upload_to = 'driver/ktp_photo', blank=True)
    profile_picture = models.ImageField(upload_to = 'driver/profile_picture', blank=True)
    is_approved = models.BooleanField(default=False)
    ad_request_approved = models.BooleanField(default=False)
    ad_installation_approved = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    forgot_token = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
    
    def __str__(self):
        return '%s - %s'%(self.full_name.title(), self.province.name.upper())
