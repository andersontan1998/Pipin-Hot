from django.urls import path
from .views import biddingMenu, deliveryUI
#from delivery import views

urlpatterns = [
    path('deliveryui/', deliveryUI.as_view(), name='deliveryui'),
    path("deliveryui/bidding/", biddingMenu.as_view(), name='bidding'),
]
