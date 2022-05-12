from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'img']


class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodItem
<<<<<<< HEAD
        fields = ['name', 'price', 'img', 'category', 'description']
        exclude = ['chef_name']
=======
        fields = ['name', 'price', 'img', 'category', 'description', 'vip_exclusive']
>>>>>>> 147462f0db99cc95dda7792d2cb2944a0411fd31
