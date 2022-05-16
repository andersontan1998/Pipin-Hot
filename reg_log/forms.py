from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError, transaction
from .models import Customer, Chef, Manager, Deliverer, SalesAssociate, User
from django import forms
from django.core.exceptions import ValidationError

BIGINT_MIN = -9223372036854775808
BIGINT_MAX = 9223372036854775807

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
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    address = forms.CharField(required=True, max_length=60)

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
    first_name = forms.CharField(required=True, max_length=30)
    salary = forms.IntegerField(required=True, min_value=BIGINT_MIN, max_value=BIGINT_MAX)
    rating = forms.IntegerField(required=True)

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
        chef.salary = self.cleaned_data.get('salary')
        chef.rating = self.cleaned_data('rating')
        chef.save()

        return user


class DelivererSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    salary = forms.IntegerField(required=True, min_value=BIGINT_MIN, max_value=BIGINT_MAX)

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
        deliverer.salary = self.cleaned_data.get('salary')
        deliverer.save()

        return user


class SalesAssociateSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    salary = forms.IntegerField(required=True, min_value=BIGINT_MIN, max_value=BIGINT_MAX)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sales = True
        user.username = self.cleaned_data.get('username')
        user.save()
        sales = SalesAssociate.objects.create(user=user)
        sales.first_name = self.cleaned_data.get('first_name')
        sales.last_name = self.cleaned_data.get('last_name')
        sales.salary = self.cleaned_data.get('salary')
        sales.save()


class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    salary = forms.IntegerField(required=True, min_value=BIGINT_MIN, max_value=BIGINT_MAX)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.username = self.cleaned_data.get('username')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.first_name = self.cleaned_data.get('first_name')
        manager.last_name = self.cleaned_data.get('last_name')
        manager.salary = self.cleaned_data.get('salary')
        manager.save()
