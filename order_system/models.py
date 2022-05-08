from unicodedata import decimal
from django.db import models
from menu.models import FoodItem

# Create your models here.


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    items = models.ManyToManyField(FoodItem, related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
