from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.forms import *
from reg_log.models import Customer, Manager, User, Chef, Deliverer
from forums.models import Review, EmployeeReview
# Create your views here.


def custDashboardView(request):
    user = request.user
    # print(user.username)
    cust = Customer.objects.get(pk=user.pk)
    # print(cust.warnings)
    return render(request, 'custDash.html', {'user': cust})


def editProfileView(request):
    user = request.user  # get user object
    cust = Customer.objects.get(pk=user)  # get customer info from user

    form = editForm(request.POST, request.FILES)  # get form for editing info

    if form.is_valid():
        # update customer object with form data
        cust.first_name = form.cleaned_data.get('first_name')
        cust.last_name = form.cleaned_data.get('last_name')
        cust.address = form.cleaned_data.get('address')
        #cust.account_funds = form.cleaned_data.get('account_funds')
        cust.save()
        return redirect('cust_dashboard')  # redirect back to dashboard
    else:
        form = editForm()

    # initial render of edit profile page
    return render(request, 'editProfile.html', {'form': form, 'user': cust})


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


def managerDashboardView(request):
    manager = Manager.objects.get(pk=request.user.pk)
    reviews = EmployeeReview.objects.all()
    # print(user.username)
    if manager is not None:
        return render(request, 'managerDash.html', {'user': manager, 'reviews': reviews})

    else:
        redirect('/reg_log/templates/index.html')
    # print(cust.warnings)


def acceptReview(request, pk):

    review = EmployeeReview.objects.get(pk=int(pk))
    employee = User.objects.get(username=review.employee_name.username)
    if employee.is_chef:
        chef = Chef.objects.get(pk=review.employee_name.pk)
        if(review.is_complaint):
            chef.rating = chef.rating - 1
        else:
            chef.rating = chef.rating + 1
        chef.save()
    elif employee.is_delivery:
        deli = Deliverer.objects.get(pk=review.employee_name.pk)
        if(review.is_complaint):
            deli.rating = deli.rating - 1
        else:
            deli.rating = deli.rating + 1
        deli.save()

    else:
        cust = Customer.objects.get(pk=review.review_order.complainee)
        if (review.is_complaint):

            cust.warnings = cust.warnings - 1

        else:
            cust.warnings = cust.warning + 1
        cust.save()

    review.delete()
    # verify that they don't surpass the warnings metric
    return redirect('manager_dashboard')


def rejectReview(request, pk):

    review = EmployeeReview.objects.get(pk=int(pk))
    reviewer = User.objects.get(username=review.review_order.complainee)
    if reviewer.is_customer:
        reviewer = Customer.objects.get(pk=review.review_order.complainee.pk)
        reviewer.warnings = reviewer.warnings - 1
        reviewer.save()

    review.delete()
    # verify that they don't surpass the warnings metric

    return redirect('manager_dashboard')
