
from django.urls import path
from .views import *

urlpatterns = [
    path('defaultHome', defaultHome, name='defaultHome'),
    path('logOut', logOut, name='logoutNav'),
    path('loginNav', loginNav, name='loginNav'),
    path('registerNav', registerNav, name='regNav'),
    path('ordersNav', ordersNav, name='ordersNav'),
    path('menuNav', menuNav, name='menuNav'),
    path('forumNav', forumNav, name='forumNav'),
    path('dashNav', dashNav, name='dashNav')
]