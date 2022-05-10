from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FoodItem
import os
  
#Create your views here.
def custFoodView(request):
    form = FoodForm(request.POST, request.FILES)
    foodList = FoodItem.objects.all()

    if form.is_valid():
        form.save()
    
    else:
        form = FoodForm()

    return render(request, 'userMenu.html', {'form': form, 'foodList': foodList})

def foodView(request):
    form = FoodForm(request.POST, request.FILES)
    foodList = FoodItem.objects.all()

    if form.is_valid():
        form.save()
        #name = form.cleaned_data['name']
        #price = form.cleaned_data['price']
        #category = form.cleaned_data['category']
        #print(name, price, category)
    else:
        form = FoodForm()

    return render(request, 'chefMenu.html', {'form': form, 'foodList': foodList})

def deleteFood(request, name):
    print(name)
    item = FoodItem.objects.get(name=name)
    if len(item.img)>0:
        os.remove(item.img.path)
    item.delete()
    return redirect('chef_menu')

