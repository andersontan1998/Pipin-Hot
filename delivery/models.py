from unicodedata import decimal
from django.db import models
from reg_log.models import User
from menu.models import FoodItem

# Create your models here.


class Bid(models.Model):
    Name = models.CharField(max_length=30, blank=True)
    Order =  models.IntegerField(default=0, primary_key=True)
    Bid_Amount = models.IntegerField(default = 100)
    lowest_bid = models.IntegerField(null = True, blank=True)
