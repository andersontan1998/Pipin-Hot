from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Customer, Chef, Deliverer
from .forms import CustSignUpForm, ChefSignUpForm, DelivererSignUpForm, SalesAssociateSignUpForm, UserTypeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def index(request, context={}):
    return render(request, 'defaultHome.html')


def register(request, context={}):
    if (request.user.is_authenticated):
        return redirect('defaultHome.html')

    utform = UserTypeForm(request.POST)
    delivform = DelivererSignUpForm()
    custform = CustSignUpForm()
    chefform = ChefSignUpForm
    context = {'ut' : ''}
    if(utform.is_valid()):
        delivform = DelivererSignUpForm()
        context = {'ut' : utform.cleaned_data['user_type']}
    else:
        utform = UserTypeForm()
        # chefform = ChefSignUpForm()
        # salesform = SalesAssociateSignUpForm()

    context['utform'] = utform
    context['delivform'] = delivform
    context['custform'] = custform
    context['chefform'] = chefform

    return render(request, 'register.html', context)


class customer_register(CreateView):
    model = User
    form_class = CustSignUpForm
    template_name = '../templates/customer_register.html'


class chef_register(CreateView):
    model = User
    form_class = ChefSignUpForm
    template_name = 'chef_register.html'


class deliverer_register(CreateView):
    model = User
    form_class = DelivererSignUpForm
    template_name = '../templates/deliverer_register.html'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'defaultHome.html')
            else:
                messages.error(request, "Incorrect username and/or password")
        else:
            messages.error(request, "Form not valid")

    # context is
    if (request.user.is_authenticated):
        return redirect('deliveryui')

    return render(request, '../templates/login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return render(request,'defaultHome.html')
