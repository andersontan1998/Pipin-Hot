from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Customer, Chef, Deliverer
from .forms import CustSignUpForm, ChefSignUpForm, DelivererSignUpForm, ManagerSignUpForm, SalesAssociateSignUpForm, UserTypeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request, context={}):
    return render(request, 'defaultHome.html')


@csrf_exempt
def register(request, context={}):
    if (request.user.is_authenticated):
        return redirect('defaultHome.html')

    if(request.method == 'POST'):
        utform = UserTypeForm(request.POST)
        delivform = DelivererSignUpForm()
        custform = CustSignUpForm()
        chefform = ChefSignUpForm()
        salesform = SalesAssociateSignUpForm()
        managerform = ManagerSignUpForm()
        context = {'ut' : ''}
        if(utform.is_valid()):
            ut = utform.cleaned_data['user_type']
            context['ut'] = ut

            if(ut == 'delivery'):
                form = DelivererSignUpForm(request.POST)
                print('hello')
            elif(ut == 'customer'):
                form = CustSignUpForm(request.POST)
            elif(ut == 'chef'):
                form = ChefSignUpForm(request.POST)
            elif(ut == 'manager'):
                form = ManagerSignUpForm(request.POST)
            else:
                form = SalesAssociateSignUpForm(request.POST)

            if (form.is_valid()):
                form.instance.is_active = False
                form.save()
                return redirect('login')
            else:
                context['form'] = form
            

    else:
        utform = UserTypeForm()
        # chefform = ChefSignUpForm()
        # salesform = SalesAssociateSignUpForm()

    context['utform'] = utform
    # context['form'] = DelivererSignUpForm()
    # context['custform'] = custform
    # context['chefform'] = chefform
    # context['salesform'] = salesform
    # context['managerform'] = managerform

    return render(request, 'register.html', context)


class customer_register(CreateView):
    model = User
    form_class = CustSignUpForm
    template_name = '../templates/customer_register.html'
    def get_success_url(self) -> str:
        return super().get_success_url()



class chef_register(CreateView):
    model = User
    form_class = ChefSignUpForm
    template_name = 'chef_register.html'
    def get_success_url(self) -> str:
        return super().get_success_url()



class deliverer_register(CreateView):
    model = User
    form_class = DelivererSignUpForm
    template_name = '../templates/deliverer_register.html'
    def get_success_url(self) -> str:
        return super().get_success_url()


class sales_register(CreateView):
    model = User
    form_class = SalesAssociateSignUpForm
    template_name = 'sales_register.html'

class manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'manager_register.html'


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
        if(Deliverer.objects.filter(pk=request.user).exists()):
            return redirect('deliveryui')

    return render(request, '../templates/login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return render(request,'defaultHome.html')
