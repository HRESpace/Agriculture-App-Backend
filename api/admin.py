from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email_id', 'date','imgUri','crop_type','crop_season', 'village_district',
                    'state','field_owner','soil_type','prev_crop','yield_history']
