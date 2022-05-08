from django.urls import path
from reg_log import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("register", views.register, name='register'),
    path('customer_register', views.customer_register.as_view(),
         name='customer_register'),
    path('chef_register', views.chef_register.as_view(),
         name='chef_register'),
    path('deliverer_register', views.deliverer_register.as_view(),
         name='deliverer_register'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name="logout")
]
