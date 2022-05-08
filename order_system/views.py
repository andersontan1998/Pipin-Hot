from django.shortcuts import render
from django.views import Views
# Create your views here.


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category

        #appeitizer = MenuItem.objects.filter(category__name__contatins='Appetizer')

        # pass into context

        context = {
            #Appetizer: Appetizer
        }
        # render template

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for items in items:
            menu_item = MenuItem.objects.get(pk=int(item))
