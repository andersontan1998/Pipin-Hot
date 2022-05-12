from django import forms
from reg_log.models import Customer

class editForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    #account_funds = forms.IntegerField()

class moneyForm(forms.Form):
    CC_Number = forms.IntegerField()
    Security_Code = forms.DecimalField(max_digits=4, decimal_places=0)
    Cardholder_Name = forms.CharField()
    Expiration_Date = forms.CharField()
    Amount_to_Add = forms.IntegerField()