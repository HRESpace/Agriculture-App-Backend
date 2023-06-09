from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', views.user_api),
    path('downloaddata/<str:email>/',views.download_data)
]