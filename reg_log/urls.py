from django.urls import path
from .import views

urlpatterns = [
    path("", views.register, name='register'),
    path('customer', views.customer_register.as_view(),
         name='customer_register'),
    path("login", views.login_view, name='login')
]
