from django.contrib import admin
from .models import Location, Brand, VehicleModel, Feature, Vehicle, Image


admin.site.register((Location, Brand, VehicleModel, Feature, Vehicle, Image))
