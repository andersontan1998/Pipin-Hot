from django.urls import path
from reg_log import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("logout", views.logout_view, name="logout")
]
