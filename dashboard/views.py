from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.forms import *
from reg_log.models import Customer
# Create your views here.

def custDashboardView(request):
    user = request.user
    #print(user.username)
    cust = Customer.objects.get(pk=user)
    #print(cust.warnings)
    return render(request, 'custDash.html', {'user': cust}) 

def editProfileView(request):
    user = request.user                     #get user object
    cust = Customer.objects.get(pk=user)    #get customer info from user

    form = editForm(request.POST, request.FILES)    #get form for editing info

    if form.is_valid():
        #update customer object with form data
        cust.first_name = form.cleaned_data.get('first_name')
        cust.last_name = form.cleaned_data.get('last_name')
        cust.address = form.cleaned_data.get('address')
        #cust.account_funds = form.cleaned_data.get('account_funds')
        cust.save()
        return redirect('cust_dashboard')   #redirect back to dashboard
    else:
        form = editForm() 

    return render(request, 'editProfile.html', {'form': form, 'user': cust})    #initial render of edit profile page 

def addFundsView(request):
    user = request.user
    cust = Customer.objects.get(pk=user)

    form = moneyForm(request.POST, request.FILES)
    
    if form.is_valid():
        print(form.cleaned_data.get('Amount_to_Add'))
        cust.account_funds = form.cleaned_data.get('Amount_to_Add')
        cust.save()
        return redirect('cust_dashboard')
    else:
        form = moneyForm()
    
    return render(request, 'editFunds.html', {'form': form, 'user': cust})
