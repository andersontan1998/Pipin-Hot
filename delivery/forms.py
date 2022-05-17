from django import forms
from reg_log.models import Deliverer

class bidForm(forms.Form):
    Deliverer_Name = forms.CharField(required=True) 
    Order_Number = forms.IntegerField()
    Bidding_Value = forms.IntegerField()