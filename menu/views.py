from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FoodItem
from reg_log.models import Customer, Chef
import os

# Create your views here.


def custFoodView(request):
    form = FoodForm(request.POST, request.FILES)
    foodList = FoodItem.objects.all()

    user = request.user
    if (Customer.objects.filter(pk=user).exists()):
        #return render(request, 'userMenu.html', {'form': form, 'foodList': foodList})
        return redirect('order')
    
    else:
        if form.is_valid():
            form.save()

        else:
            form = FoodForm()

        return render(request, 'userMenu.html', {'form': form, 'foodList': foodList})
        #return redirect('order')


def foodView(request):
    form = FoodForm(request.POST, request.FILES)
    foodList = FoodItem.objects.all()
    topFoods = FoodItem.objects.order_by('rating')[3:]
    user = request.user

    if (Chef.objects.filter(pk=user).exists()):
        #print("MASTER CHEF DETECTED")
        if form.is_valid():
            foodItem = form.save(commit=False)
            foodItem.chef_name = User.objects.get(pk=request.user.pk)
            foodItem.save()
        else:
            form = FoodForm()

        return render(request, 'chefMenu.html', {'form': form, 'foodList': foodList, 'topfoodList': topFoods})
    else:
        #print("Not a Chef!")
        return redirect('default')
        
def deleteFood(request, name):
    print(name)
    item = FoodItem.objects.get(name=name)
    if len(item.img) > 0:
        os.remove(item.img.path)
    item.delete()
    return redirect('chef_menu')
