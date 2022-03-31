from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    added_by = serializers.CharField(read_only=True)
    added_by_id = serializers.IntegerField(write_only=True)
    model = serializers.CharField(read_only=True)
    model_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Vehicle
        fields = "__all__"