from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product") or None
        super.__init__(*args, **kwargs)
        self.product = product

    class Meta:
        model = Order
        fileds = [
            "shipping_address",
            "billing_address"
        ]
    
    def clean(self, *args, **kwargs):
        cleaned_data = super.clean(*args, **kwargs)

        return cleaned_data