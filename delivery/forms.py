from django import forms
from reg_log.models import Deliverer

class bidForm(forms.Form):
    Order_Number = forms.IntegerField()
    Place_Bid = forms.IntegerField()