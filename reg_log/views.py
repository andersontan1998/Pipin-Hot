from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import CustSignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register(request):
    return render(request, '../templates/register.html')


class customer_register(CreateView):
    model = User
    form_class = CustSignUpForm
    template_name = '../templates/customer.html'


def login_view(request):
    # context is
    return render(request, '../templates/login.html', context={'form': AuthenticationForm()})
