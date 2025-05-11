from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Role
# SystemSetting, AuditLog, PlatformConfiguration, APIKey


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


# class SystemSettingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SystemSetting
#         fields = '__all__'


# class AuditLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuditLog
#         fields = '__all__'


# class PlatformConfigurationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlatformConfiguration
#         fields = '__all__'


# class APIKeySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = APIKey
#         fields = '__all__'
