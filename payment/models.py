from django.db import models

class BankName(models.Model):
	bank_name = models.CharField(max_length=60)
	def __str__(self):
		return self.bank_name.title()

class BankAccount(models.Model):
	bank_name = models.CharField(max_length=60)
	bank_branch_name = models.CharField(max_length=200, null=True, blank=True)
	bank_account_number = models.CharField(max_length=30)
	bank_account_name = models.CharField(max_length=60, null=True, blank=True)
	on_behalf = models.CharField(max_length=60, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return '%s : %s'%(self.bank_name.upper(), self.bank_account_number.upper())

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
