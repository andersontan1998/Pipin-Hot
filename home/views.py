from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def defaultHome(request):
    return render(request, 'defaultHome.html')

@login_required(redirect_field_name='defaultHome.html')
def loggedinHome(request):
    return render(request, 'loggedinHome.html')

def loginNav(request):
    return redirect('login')

def ordersNav(request):
    return redirect('order')

def menuNav(request):
    return redirect('customer_menu')

def forumNav(request):
    return redirect('forum')

def dashNav(request):
    return redirect('cust_dashboard')