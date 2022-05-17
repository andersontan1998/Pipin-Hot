from tkinter import CASCADE
from django.db import models
from numpy import True_
from reg_log.models import User
from order_system.models import OrderModel

# Create your models here.


class Forum_Posts(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    article_content = models.CharField(default=0, max_length=100)
    subject = models.CharField(max_length=50)
    rating = models.IntegerField(default=10)


class Review(models.Model):
    complainee = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    reviewed_by_manager = models.BooleanField(default=False)
    order_assigned = models.ForeignKey(
        OrderModel, on_delete=models.CASCADE, blank=True, null=True)


class EmployeeReview(models.Model):
    review_order = models.ForeignKey(
        Review, on_delete=models.CASCADE, blank=True)
    is_complaint = models.BooleanField(default=False, blank=True)
    employee_name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=100, blank=True)
    # ADD ITEM ASSOCIATED
