from dataclasses import fields
from django.forms import ModelForm
from django import forms
from models import Forum_Posts


class PostForm(ModelForm):
    class Meta:
        model = Forum_Posts
        fields = ['post_user', 'article_content',
                  'subject', 'rating', 'reviewed_by_manager']
