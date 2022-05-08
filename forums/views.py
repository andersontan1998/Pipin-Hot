from django.shortcuts import render
from django.views import generic
from forums.models import Forum_Posts

# Create your views here.

# @login_Required


class index(generic.ListView):
    model = Forum_Posts

    template_name = 'index.html'

    def get_queryset(self):
        return Forum_Posts.objects.all()
