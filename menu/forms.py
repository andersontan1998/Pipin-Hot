from django import forms
from .models import *
  
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'img']

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'price', 'img', 'category', 'description']