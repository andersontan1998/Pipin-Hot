from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from pandas import DatetimeIndex
from order_system.models import OrderModel

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
        
class biddingMenu(View):
    def get(self, request, *args, **kwargs):

        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)


        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
        }

        return render(request, '../templates/biddingMenu.html', context)


#def biddingMenu(request):
#    return render(request, '../templates/biddingMenu.html')
        