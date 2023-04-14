from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.

class User(models.Model):
    date = models.CharField(max_length=10)
    user_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=100)
    imgUri = models.CharField(max_length=2000)
    crop_type = models.CharField(max_length=50)
    crop_season = models.CharField(max_length=50)
    village_district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    field_owner = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=50)
    prev_crop = models.CharField(max_length=50)
    yield_history = models.CharField(max_length=250)
