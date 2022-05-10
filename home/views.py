from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
def defaultHome(request):
    return render(request, 'defaultHome.html')

def loginNav(request):
    return redirect('login')

def ordersNav(request):
    return redirect('order')

def menuNav(request):
    return redirect('customer_menu')