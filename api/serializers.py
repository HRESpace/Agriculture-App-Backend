from rest_framework import serializers
from .models import User
from django.core.validators import MaxLengthValidator


class UserSerializers(serializers.Serializer):
    # date = serializers.DateField(validators=[MaxLengthValidator(10)])
    # time = serializers.TimeField(validators=[MaxLengthValidator(5)])
    date = serializers.CharField(max_length=10)
    time = serializers.CharField(max_length=5)
    user_name = serializers.CharField(max_length=50)
    imgUri = serializers.CharField(max_length=2000)
    crop_type = serializers.CharField(max_length=50)
    crop_season = serializers.CharField(max_length=50)
    crop_stage = serializers.CharField(max_length=250)
    plot_area = serializers.FloatField()
    village = serializers.CharField(max_length=50)
    district_or_mandal_name = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    field_owner = serializers.CharField(max_length=50)
    land_type = serializers.CharField(max_length=50)
    soil_type = serializers.CharField(max_length=50)
    soil_moisture = serializers.CharField(max_length=50)
    prev_crop = serializers.CharField(max_length=50)
    approx_yield = serializers.FloatField()
    yield_history = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
