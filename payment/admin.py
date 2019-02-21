from django.contrib import admin
from .models import BankName, BankAccount

class BankNameAdmin(admin.ModelAdmin):
    model = BankName
class BankAccountAdmin(admin.ModelAdmin):
    model = BankAccount

admin.site.register(BankName, BankNameAdmin)
admin.site.register(BankAccount, BankAccountAdmin)