from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'date','time','imgUri','crop_type','crop_season','crop_stage','plot_area',
                    'village','district_or_mandal_name','state','field_owner','land_type','soil_type',
                    'soil_moisture','prev_crop','approx_yield','yield_history']
