from rest_framework import serializers
from .models import Courier, CourierPerformance


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class CourierPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierPerformance
        fields = '__all__'
