from django.urls import path
from .views import *

urlpatterns = [
    path('defaultHome', defaultHome, name='defaultHome'),
    path('logOutButton', logOutButton, name='logOutButton'),
    path('ordersNav', ordersNav, name='ordersNav')
]