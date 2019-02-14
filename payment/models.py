from django.db import models

class BankAccount(models.Model):
	bank_name = models.CharField(max_length=30)
	bank_branch_name = models.CharField(max_length=30)
	bank_account_number = models.CharField(max_length=30)
	bank_account_name = models.CharField(max_length=50)
	on_behalf = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)

class Payment(models.Model):
	driver_name = models.CharField(max_length=50, null=True)
	periode = models.IntegerField()
	license_no = models.CharField(max_length=10, null=True)
	vehicle_type = models.CharField(max_length=20, null=True)
	campaign_name = models.CharField(max_length=50, null=True)
	mileage = models.IntegerField()
	verified_date = models.DateTimeField(null=True)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)
	is_verified = models.BooleanField(default=False)

	def __str__(self):
		return self.driver_name.title()
