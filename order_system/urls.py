from django.urls import path
from order_system import views

urlpatterns = [
    path("order", views.Order.as_view(), name='order'),
    path("order_confirmation/<int:pk>", views.OrderConfirmation.as_view(),
         name="order_confirmation"),

    #path("logout", views.logout_view, name="logout")
]
