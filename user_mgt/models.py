from django.db import models
from django.contrib.auth.models import User

# class UserType(models.Model):
#     name = models.CharField(max_length=15, blank=True)    

#     class Meta:
#         verbose_name = "User Type"
#         verbose_name_plural = "User Types"
    
#     def __str__(self):
#         return self.name

class Privilege(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Privilege"
        verbose_name_plural = "Privileges"
    
    def __str__(self):
        return self.name

class UserRole(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    privilege = models.ManyToManyField(Privilege)
    is_archived = models.BooleanField(default=False)
    class Meta:
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"
    
    def __str__(self):
        return self.name

class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default='')
    mobile_phone = models.CharField(max_length=20, default='')
    role = models.ManyToManyField(UserRole, db_index=True)
    profile_picture = models.ImageField(upload_to = 'bo/profile_picture', blank=True)
    status = models.CharField(max_length=255, default='')
    forgot_token = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    class Meta:
        verbose_name = "User Management"
        verbose_name_plural = "Users Management"
    
    def __str__(self):
        return self.user.username
