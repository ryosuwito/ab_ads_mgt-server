from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    name = models.CharField(max_length=15, blank=True)    

    class Meta:
        verbose_name = "User Type"
        verbose_name_plural = "User Types"
    
    def __str__(self):
        return self.name

class Privilege(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = "Privilege"
        verbose_name_plural = "Privileges"
    
    def __str__(self):
        return self.name

class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.ForeignKey(UserType, on_delete=models.SET_NULL, db_index=True, null=True)
    privilege_user = models.ForeignKey(Privilege, on_delete=models.SET_NULL, db_index=True, null=True)
    status = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = "User Management"
        verbose_name_plural = "Users Management"
    
    def __str__(self):
        return self.user.username