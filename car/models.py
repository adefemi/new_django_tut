from ast import mod
from django.db import models


class DateControls(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Manufacturer(DateControls):
    name = models.CharField(max_length=200, help_text="holds the name of the car", unique=True)
    
    def __str__(self):
        return self.name


class Car(DateControls):
    name = models.CharField(max_length=200, help_text="holds the name of the car")
    model = models.CharField(max_length=50, choices=(('v8', 'v_8'), ('v6', 'v_6'), ('v4', 'v_4')))
    serial_number = models.PositiveBigIntegerField(unique=True)
    manufacture_date = models.DateTimeField()
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="car_manufacturers", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"
    
    
