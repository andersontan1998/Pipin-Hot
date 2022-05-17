from operator import is_
from django.shortcuts import redirect, render
from django.views import generic
from forums.models import Forum_Posts
from menu.models import FoodItem
from order_system.models import OrderModel
from django.views import View
from forums.models import Review, EmployeeReview
from reg_log.models import User

# Create your views here.

# @login_Required


class all_orders(generic.ListView):
    def get(self, request, *args, **kwargs):
        # get every item from each category

        template_name = 'forum.html'
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

        user = User.objects.get(pk=request.user.pk)
        order_pk = request.POST.get('order')
        review = Review.objects.create(
            complainee=user, reviewed_by_manager=False, order_assigned=OrderModel.objects.get(pk=order_pk))

        return redirect("review", pk=review.pk)


class review(View):

    def get(self, request, pk, *args, **kwargs):

        review = Review.objects.get(pk=pk)
        order = OrderModel.objects.get(pk=review.order_assigned.pk)
        is_delivery = order.is_delivery

        context = {
            'review': review,
            'order': order,
            'is_delivery': is_delivery

        }

        return render(request, "review.html", context)

    def post(self, request, pk, *args, **kwargs):

        user = User.objects.get(pk=request.user.pk)
        review = Review.objects.get(pk=pk)
        items = request.POST.getlist('items[]')

        if (review.order_assigned.is_delivery):

            description = request.POST.get("description")
            is_complaint = False
            selection = request.POST.get('review delivery')
            if "complain" == selection:
                is_complaint = True

            else:
                is_complaint = False

            delivery_review = EmployeeReview.objects.create(review_order=review,
                                                            is_complaint=is_complaint, employee_name=None, description=description)
            for item in items:
                menu_item = FoodItem.objects.get(pk=int(item))
                rating = request.POST.get(menu_item.name)
                menu_item.rating = menu_item.rating + int(rating)
                menu_item.quantity_ordered = menu_item.quantity_ordered + 1
                menu_item.save()

        else:
            for item in items:
                menu_item = FoodItem.objects.get(pk=int(item))

                selection = request.POST.get(
                    menu_item.chef_name.username+','+menu_item.name)
                description = request.POST.get(
                    "description," + str(menu_item.pk))

                # {{item.chef_name.username}},{{item.name}}
                if "complain" == selection:
                    is_complaint = True
                else:
                    is_complaint = False

                EmployeeReview.objects.create(review_order=review,
                                              is_complaint=is_complaint, employee_name=menu_item.chef_name, description=description)

                rating = request.POST.get(menu_item.name)
                menu_item.rating = menu_item.rating + int(rating)
                menu_item.quantity_ordered = menu_item.quantity_ordered + 1
                menu_item.save()
        # review_employee = Complaint.objects.create(
        #     complainee=request.user, description=description, is_delivery=is_delivery)

        return redirect("all_orders")


# class review_confirmation

# class deliverer_register(CreateView):
#     model = User
#     form_class = DelivererSignUpForm
#     template_name = '../templates/deliverer_register.html'
