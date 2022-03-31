from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import VehicleSerializer, Vehicle


class VehicleView(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer