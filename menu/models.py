from django.db import models
from reg_log.models import User
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
<<<<<<< HEAD
    chef_name = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, default=None)
=======
    vip_exclusive = models.BooleanField(default=False)
>>>>>>> 147462f0db99cc95dda7792d2cb2944a0411fd31


class Image(models.Model):
    caption = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads/')


# class TopThree(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
#     item = models.OneToOneField(FoodItem, on_delete=models.CASCADE, blank=True)
#     count = models.IntegerField(default=0)
#     rating = models.IntegerField(defualt=0)


def __str__(self):
    return self.title
