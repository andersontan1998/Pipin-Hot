from django.urls import path
from .views import deliveryUI

urlpatterns = [
    path('deliveryui/', deliveryUI.as_view(), name='deliveryui'),
]
