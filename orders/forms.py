from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fileds = [
            "shipping_address",
            "billing_address"
        ]