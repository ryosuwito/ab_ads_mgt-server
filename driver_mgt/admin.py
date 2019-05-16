from django.contrib import admin
from .models import Driver, BuktiTayang

class DriverAdmin(admin.ModelAdmin):
    model = Driver
class BuktiTayangAdmin(admin.ModelAdmin):
    model = BuktiTayang

admin.site.register(BuktiTayang, BuktiTayangAdmin)
admin.site.register(Driver, DriverAdmin)