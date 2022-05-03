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

    is_customer = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_deliverer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)


class Customer(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    account_funds = models.IntegerField()


class Chef(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    salary = models.BigIntegerField()
    rating = models.IntegerField()


class Deliverer(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    salary = models.BigIntegerField()


class Manager(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.BigIntegerField()
