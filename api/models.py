from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.

class User(models.Model):
    # date = models.DateField(validators=[MaxLengthValidator(10)])
    date = models.CharField(max_length=10)
    # time = models.TimeField(validators=[MaxLengthValidator(5)])
    time = models.CharField(max_length=5)
    user_name = models.CharField(max_length=50)
    imgUri = models.CharField(max_length=2000)
    crop_type = models.CharField(max_length=50)
    crop_season = models.CharField(max_length=50)
    crop_stage = models.CharField(max_length=250)
    plot_area = models.FloatField()
    village = models.CharField(max_length=50)
    district_or_mandal_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    field_owner = models.CharField(max_length=50)
    land_type = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=50)
    soil_moisture = models.CharField(max_length=50)
    prev_crop = models.CharField(max_length=50)
    approx_yield = models.FloatField()
    yield_history = models.CharField(max_length=250)
