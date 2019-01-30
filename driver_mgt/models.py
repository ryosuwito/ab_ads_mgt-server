from django.db import models

from user_mgt.models import UserManagement
from area_db.models import Province, City, Kecamatan, Kelurahan

class Driver(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(UserManagement, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, db_index=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, db_index=True, null=True)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.SET_NULL, db_index=True, null=True)
    ktp_photo = models.ImageField(upload_to = 'driver/ktp_photo', blank=True)
    bank_name = models.CharField(max_length=30)
    bank_branch_name = models.CharField(max_length=30)
    bank_account_number = models.CharField(max_length=30)
    bank_account_name = models.CharField(max_length=50)