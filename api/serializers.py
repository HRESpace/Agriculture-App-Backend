from rest_framework import serializers
from .models import User
from django.core.validators import MaxLengthValidator


class UserSerializers(serializers.Serializer):
    date = serializers.CharField(max_length=10)
    user_name = serializers.CharField(max_length=50)
    email_id = serializers.CharField(max_length = 100)
    imgUri = serializers.CharField(max_length=2000)
    crop_type = serializers.CharField(max_length=50)
    crop_season = serializers.CharField(max_length=50)
    village_district = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=50)
    field_owner = serializers.CharField(max_length=50)
    soil_type = serializers.CharField(max_length=50)
    prev_crop = serializers.CharField(max_length=50)
    yield_history = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def validate_plot_area(self, value):
        if value <= 0:
            raise serializers.ValidationError("plot_area must be a positive value")
        return value
