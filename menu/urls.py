from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('image_upload/', imgView, name = 'image_upload'),
    path('success/', uploadok, name = 'success'),
    path('chefMenu/', foodView, name = 'chef_menu'),
    path('deleteFood/<name>', deleteFood, name = 'deleteFood'),
    path('userMenu/', custFoodView, name = 'customer_menu'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)