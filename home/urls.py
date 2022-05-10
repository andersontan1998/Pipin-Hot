from django.urls import path
from .views import *

urlpatterns = [
    path('defaultHome', defaultHome, name='default')
]