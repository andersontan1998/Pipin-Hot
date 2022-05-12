from django.shortcuts import render, redirect
from django.views import View
from order_system.models import OrderModel
from menu.models import FoodItem
import json
from reg_log.models import User
# Create your views here.


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category

        appetizer = FoodItem.objects.filter(
            category__startswith='Dinner')

        user = User.objects.get(pk=request.user.pk)

        # pass into context

        context = {
            'Appetizer': appetizer,
            'User': user
        }
        # render template
        return render(request, 'order.html', context)

    def post(self, request, *args, **kwargs):

        user = User.objects.get(pk=request.user.pk)
        name = user.username

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = FoodItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

        price = 0
        items_id = []

        for item in order_items['items']:
            price += item['price']
            items_id.append(item['id'])

        logistic = request.POST.get("logistic")

        if logistic == "delivery":
            order = OrderModel.objects.create(
                price=price, name=name, is_delivery=True)

        else:
            order = OrderModel.objects.create(
                price=price, name=name, is_delivery=False)

        order.items.add(*items_id)

        return redirect("order_confirmation", pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'items': order.items,
            'price': order.price,
            'pk': order.pk
        }

        return render(request, 'order_confirmation.html', context)

    # def post(self, request, pk, *args, **kwargs):
    #     data = json.loads(request.body)

    #     return redirect('payment-confirmation')
