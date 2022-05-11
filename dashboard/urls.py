from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
        path('customer/', custDashboardView, name = 'cust_dashboard'),
        path('editProfile/', editProfileView, name = 'edit_profile'),
        path('editFunds/', addFundsView, name = 'edit_funds'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 