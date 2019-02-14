from django.contrib import admin
from .models import MainRoute

class MainRouteAdmin(admin.ModelAdmin):
    model = MainRoute

admin.site.register(MainRoute, MainRouteAdmin)
