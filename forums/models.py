from tkinter import CASCADE
from django.db import models
from reg_log.models import User
from order_system.models import OrderModel

# Create your models here.


class Forum_Posts(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    article_content = models.CharField(default=0, max_length=100)
    subject = models.CharField(max_length=50)
    rating = models.IntegerField(default=10)


class Review(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=10, blank=True)
    is_complaint = models.BooleanField(default=False, blank=True)
    subject = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=100, blank=True)
    reviewed_by_manager = models.BooleanField(default=False)
    complainee = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
