from unicodedata import decimal
from django.db import models

# Create your models here.


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #items = models.ManyToManyField('MenuItem', related_name = 'order', blank=True)

    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(Self):
        return f'Order: {self.created_on.strftime("%b %d %I, %M %p")}'
