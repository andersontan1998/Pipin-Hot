from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError, transaction
from .models import Customer, Chef, Manager, Deliverer, SalesAssociate, User
from django import forms
from django.core.exceptions import ValidationError


class UserTypeForm(forms.Form):
    user_choices = [
    ('customer', 'Customer'),
    ('chef', 'Chef'),
    ('delivery', 'Delivery'),
    ('manager', 'Manager'),
    ('sales', 'Sales Associate')
    ]
    user_type = forms.ChoiceField(required=True, label=('Register as:'), choices=user_choices)


class CustSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.username = self.cleaned_data.get('username')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.first_name = self.cleaned_data.get('first_name')
        customer.last_name = self.cleaned_data.get('last_name')
        customer.address = self.cleaned_data.get('address')
        customer.account_funds = 0
        customer.save()

        return user


class ChefSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_chef = True
        user.username = self.cleaned_data.get('username')
        user.save()
        chef = Chef.objects.create(user=user)
        chef.first_name = self.cleaned_data.get('first_name')
        chef.save()

        return user


class DelivererSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_deliverer = True
        user.username = self.cleaned_data.get('username')
        user.save()
        deliverer = Deliverer.objects.create(user=user)
        deliverer.first_name = self.cleaned_data.get('first_name')
        deliverer.save()

        return user


class SalesAssociateSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commi=False)
        user.is_sales = True
        user.username = self.cleaned_data.get('username')
        user.save()
        sales = SalesAssociate.objects.create(user=user)
        sales.first_name = self.cleaned_data.get('first_name')
        sales.save()
