from django.db import models

class Province(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    provinsi = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='kota_provinsi')
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

class Kecamatan(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    kota = models.ForeignKey(City, on_delete=models.CASCADE, related_name='kecamatan_kota')
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Kecamatan"
        verbose_name_plural = "Kecamatan"
    
    def __str__(self):
        return self.name

class Kelurahan(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    postal_code = models.CharField(max_length=20)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, related_name='kelurahan_kecamatan')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name