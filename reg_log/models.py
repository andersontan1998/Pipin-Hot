from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# class Task(models.Model):
#   class Meta:
#       permission = [
#           ("change_tast_status", "Can do something"),
#           ("close_task", "something else")
#           ]
#
#

class User(AbstractUser):
    user_choices = [
    ('customer', 'Customer'),
    ('chef', 'Chef'),
    ('delivery', 'Delivery'),
    ('manager', 'Manager'),
    ('sales', 'Sales Associate')
    ]

    is_customer = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_deliverer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_sales = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)
    user_type = models.CharField(max_length=30, choices=user_choices, blank=True)


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    account_funds = models.IntegerField(default=0)
    warnings = models.IntegerField(default=0)
    is_vip = models.BooleanField(default=False)
    # top_three = models.OneToOneField(
    #     TopThree, on_delete=models.CASCADE, blank=True)


class Chef(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    salary = models.BigIntegerField(default=0)
    rating = models.IntegerField(default=0)


class Deliverer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    salary = models.BigIntegerField(default=0)


class Manager(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.BigIntegerField()


class SalesAssociate(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.BigIntegerField()