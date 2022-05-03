from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Chef, Manager, Deliverer, User
from django import forms
from django.core.exceptions import ValidationError


class CustSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('first_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.first_name = self.cleaned_data.get('first_name')
        customer.last_name = self.cleaned_data.get('last_name')
        customer.save()

        return customer
