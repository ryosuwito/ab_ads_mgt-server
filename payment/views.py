from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from driver_mgt.models import Driver
from .models import BankName, BankAccount

class AddBankAccount(View):
	bank_names = BankName.objects.all().order_by('bank_name')
	def post(self, request, *args, **kwargs):
		bank_name = request.POST.get('bank_name')
		account_name = request.POST.get('account_name')
		bank_branch = request.POST.get('bank_branch')
		account_number = request.POST.get('account_number')
		on_behalf = request.POST.get('on_behalf')
		driver_pk = request.POST.get('account_owner')
		bank_account = ''
		if bank_name and account_number:
			bank_account = BankAccount.objects.create(
				bank_name = bank_name,
				bank_branch_name = bank_branch,
				bank_account_number = account_number,
				bank_account_name = account_name,
				on_behalf = on_behalf,
				)
		if bank_account:
			try:
				driver = Driver.objects.get(pk=driver_pk)
				driver.bank_account = bank_account
				driver.save()
			except Exception as e:
				print(e)
				return HttpResponseRedirect(reverse('payment:add_new'))
			return HttpResponseRedirect(reverse('driver:regis_driver'))
		else:
			return render(request, 
				'backend/registration/add_bank_account.html',
				{'bank_names': self.bank_names})

	def get(self, request, *args, **kwargs):
		driver_pk = request.GET.get('driver_pk')
		if driver_pk:
			driver = Driver.objects.filter(pk = driver_pk)
		else:
			driver = Driver.objects.filter(is_active=True)
		return render(request, 
			'backend/registration/add_bank_account.html',
			{'bank_names': self.bank_names,
			'drivers': driver})