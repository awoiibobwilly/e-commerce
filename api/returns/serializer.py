from rest_framework import serializers
from .models import Returns


class ReturnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Returns
        fields = '__all__'
