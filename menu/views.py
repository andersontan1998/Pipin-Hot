from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FoodItem
  
#Create your views here.
def imgView(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'imageForm.html', {'form' : form})
  
def uploadok(request):
    return HttpResponse(' upload successful')

def foodView(request):
    form = FoodForm(request.POST, request.FILES)
    foodList = FoodItem.objects.all()

    if form.is_valid():
        form.save()
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        category = form.cleaned_data['category']

        print(name, price, category)
    else:
        form = FoodForm()

    return render(request, 'chefMenu.html', {'form': form, 'foodList': foodList})

