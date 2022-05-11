from dataclasses import fields
from django.forms import ModelForm
from django import forms
from models import Forum_Posts, Review


class PostForm(ModelForm):
    class Meta:
        model = Forum_Posts
        fields = ['post_user', 'article_content',
                  'subject', 'rating', 'reviewed_by_manager']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'is_complaint',
                  'subject', 'reviewd_by_manager']
