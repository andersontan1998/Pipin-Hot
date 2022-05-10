from django.urls import path
from forums import views


urlpatterns = [
    path("all_orders", views.all_orders.as_view(), name='all_orders'),
    path("review/<int:pk>", views.review.as_view(), name='review')
]
