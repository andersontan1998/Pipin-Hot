from django.urls import path
from .views import *

urlpatterns = [
    path('defaultHome', defaultHome, name='defaultHome'),
    path('loggedinHome', loggedinHome, name='loggedinHome'),
    path('loginNav', loginNav, name='loginNav'),
    path('ordersNav', ordersNav, name='ordersNav'),
    path('menuNav', menuNav, name='menuNav'),
    path('forumNav', forumNav, name='forumNav')
]