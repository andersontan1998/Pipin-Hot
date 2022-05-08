from tkinter import CASCADE
from django.db import models
from reg_log.models import User

# Create your models here.


class Forum_Posts(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    article_content = models.CharField(default=0, max_length=100)
    subject = models.CharField(max_length=50)
    rating = models.IntegerField(default=10)
    reviewed_by_manager = models.BooleanField(default=False)
