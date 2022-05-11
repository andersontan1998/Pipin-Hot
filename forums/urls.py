from django.urls import path
from forums import views

urlpatterns = [
    path("forum", views.index.as_view(), name='forum')
]
