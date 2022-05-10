from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def defaultHome(request):
    return render(request, 'defaultHome.html')

def logOutButton(request):
    logout(request)
    return redirect('login')

def ordersNav(request):
    return redirect('order')