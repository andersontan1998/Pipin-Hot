from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Customer, Chef, Deliverer
from .forms import CustSignUpForm, ChefSignUpForm, DelivererSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'defaultHome.html')


def register(request):
    if (request.user.is_authenticated):
        return redirect('defaultHome.html')
    return render(request, 'register.html')


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
    return render(request, '../templates/login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return render(request,'defaultHome.html')
