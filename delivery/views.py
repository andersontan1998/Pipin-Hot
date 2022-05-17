from django.shortcuts import render,redirect
from django.views import View
from django.utils.timezone import datetime
from pandas import DatetimeIndex
from order_system.models import OrderModel
from delivery.forms import *
from delivery.models import *
from reg_log.models import *


# Create your views here.

class deliveryUI(View):
    def get(self, request, *args, **kwargs):

        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value, check if order is not shipped
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        
        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, '../templates/deliveryUI.html', context)

def biddingMenu(request):

    #user = User.objects.get(pk=request.user.pk)  
    #bid = request.Bid.Order

    bid = Bid()

    allbids = Bid.objects.all()

    # get the current date
    today = datetime.today()
    orders = OrderModel.objects.filter(
        created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

    form = bidForm(request.POST, request.FILES)
    
    if form.is_valid():
        print(form.cleaned_data.get('Bidding_Value'))
        bid.Bid_Amount = form.cleaned_data.get('Bidding_Value')
        print(form.cleaned_data.get('Order_Number'))
        bid.Order = form.cleaned_data.get('Order_Number')
        print(form.cleaned_data.get('Deliverer_Name'))
        bid.Name = form.cleaned_data.get('Deliverer_Name')
        bid.save()
        return redirect('deliveryui')
    else:
        form = bidForm()

    #x = bid.Bid_Amount
    #print(x)
    
    # pass total number of orders and total revenue into template
    context = {
        'orders': orders,
        'form' : form,
        #'bidamount' : bid.Bid_Amount,
        'allbids' : allbids,
    }

    return render(request, '../templates/biddingMenu.html', context)
    
    
'''def bidNow(request):
    
    bid = Bid.objects.all()
    
    # get the current date
    today = datetime.today()
    orders = OrderModel.objects.filter(
        created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

    form = bidForm(request.POST, request.FILES)
    
    if form.is_valid():
        print(form.cleaned_data.get('Place_Bid'))
        bid.Bid_Amount = form.cleaned_data.get('Place_Bid')
        print(form.cleaned_data.get('Order_Number'))
        bid.Order = form.cleaned_data.get('Order_Number')
        bid.save()
        return redirect('deliveryui')
    else:
        form = bidForm()

    
    # pass total number of orders and total revenue into template
    context = {
        'orders': orders,
        'form' : form
    }

    return render(request, '../templates/biddingMenu.html', context)'''


#def biddingMenu(request):
#    return render(request, '../templates/biddingMenu.html')


'''class biddingMenu(View):
    def get(self, request, *args, **kwargs):
        
        bid = Bid.objects.all()
        
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        form = bidForm(request.POST, request.FILES)
        
        if form.is_valid():
           # print(form.cleaned_data.get('Place_Bid'))
            #bid.Bid_Amount = form.cleaned_data.get('Place_Bid')
            #print(form.cleaned_data.get('Order_Number'))
            #bid.Order = form.cleaned_data.get('Order_Number')
            #bid.save()
            return redirect('deliveryui')
        else:
            form = bidForm()

        
        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'form' : form
        }

        return render(request, '../templates/biddingMenu.html', context)
'''