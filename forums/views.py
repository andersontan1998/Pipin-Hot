from django.shortcuts import redirect, render
from django.views import generic
from forums.models import Forum_Posts
from menu.models import FoodItem
from order_system.models import OrderModel
from django.views import View
from forums.models import Review

# Create your views here.

# @login_Required


class all_orders(generic.ListView):
    def get(self, request, *args, **kwargs):
        # get every item from each category

        if request.user.is_authenticated:
            username = request.user.username
            orders = OrderModel.objects.filter(
                name__startswith=username)

        # pass into context

        context = {
            'Orders': orders
        }
        # render template
        return render(request, 'all_orders.html', context)

    def post(self, request, *args, **kwarg):

        order_pk = request.POST.get('order')
        order = OrderModel.objects.get(pk=order_pk)
        review = Review.objects.create(order=order)

        return redirect("review", pk=review.pk)


class review(View):

    def get(self, request, pk, *args, **kwargs):

        review = Review.objects.get(pk=pk)

        context = {
            'review': review
        }

        return render(request, "review.html", context)

    def post(self, request, pk, *args, **kwargs):

        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = FoodItem.objects.get(pk=int(item))
            rating = request.POST.get(menu_item.name)
            menu_item.rating = menu_item.rating + int(rating)
            menu_item.quantity_ordered = menu_item.quantity_ordered + 1
            menu_item.save()

        return redirect("all_orders")


# class review_confirmation

# class deliverer_register(CreateView):
#     model = User
#     form_class = DelivererSignUpForm
#     template_name = '../templates/deliverer_register.html'
