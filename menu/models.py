from django.db import models

# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField(upload_to='uploads/')
    category = models.CharField(max_length=50)
    description = models.CharField(
        max_length=300, default="No description given")
    quantity_ordered = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


class Image(models.Model):
    caption = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads/')


def __str__(self):
    return self.title
