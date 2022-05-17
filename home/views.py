
from reg_log.models import Manager, Deliverer, Chef, User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def defaultHome(request):

    if request.user.pk:
        user = User.objects.get(pk=request.user.pk)
        is_chef = user.is_chef
        context = {
            'user': user,
            'is_chef': is_chef

        }
        return render(request, 'defaultHome.html', context)

    return render(request, 'defaultHome.html')

# @login_required(redirect_field_name='defaultHome.html')
# def loggedinHome(request):
#     return render(request, 'loggedinHome.html')


@login_required(redirect_field_name='defaultHome.html')
def logOut(request):
    logout(request)
    return redirect('defaultHome')


def loginNav(request):
    return redirect('login')


def registerNav(request):
    return redirect('register')


def ordersNav(request):
    return redirect('order')


def menuNav(request):
    return redirect('customer_menu')


def forumNav(request):
    return redirect('all_orders')


def dashNav(request):
    user = request.user.pk
    if Manager.objects.filter(pk=user).exists():
        return redirect('manager_dashboard')
    if Deliverer.objects.filter(pk=user).exists():
        return redirect('deliveryui')
    if Chef.objects.filter(pk=user).exists():
        return redirect('chefMenu')
    return redirect('cust_dashboard')
