from django.urls import path
from forums import views

urlpatterns = [
    path("index", views.index.as_view(), name='index')
]
