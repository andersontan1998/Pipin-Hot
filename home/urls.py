from django.urls import path
from .views import *

urlpatterns = [
    path('defaultHome', defaultHome, name='defaultHome'),
    path('loginButton', loginButton, name='loginButton'),
    path('ordersNav', ordersNav, name='ordersNav'),
    path('menuNav', menuNav, name='menuNav')
]