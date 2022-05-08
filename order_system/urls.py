from django.urls import path
from order_system import views

urlpatterns = [
    path("order", views.Order.as_view(), name='order'),
    #path("logout", views.logout_view, name="logout")
]
