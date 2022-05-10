from django.http import HttpResponse
from django.shortcuts import render, redirect
import os;
from reg_log.models import Customer
# Create your views here.

def custDashboardView(request):
    user = request.user
    #print(user.username)
    cust = Customer.objects.get(pk=user)
    #print(cust.warnings)
    return render(request, 'custDash.html', {'user': cust}) 