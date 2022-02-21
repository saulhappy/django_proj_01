from unicodedata import decimal
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from products.models import Product

from decimal import *

# Create your models here.

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('completed', 'Completed'),
    ('refunded', 'Refunded')
)

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='created')
    sub_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def mark_paid(self, custom_amount=False, save=False):
        paid_amount = self.total
        if custom_amount: paid_amount = custom_amount
        self.paid = paid_amount
        self.status = "paid"
        if self.product: self.product.decrement_inventory(save=True)
        if save: self.save()
        return self.paid


    def calculate(self, save=False):
        if not self.product: return {}

        subtotal = round(self.product.price, 2)
        tax_rate = Decimal(0.0825)
        tax_total = round((subtotal * tax_rate), 2)
        total = round((subtotal + tax_total), 2)

        totals = {
            "subtotal": subtotal,
            "tax": tax_total,
            "total": total
        }

        for k, v in totals.items():
            setattr(self, k, v)
            if save == True: self.save()
        return totals

def order_pre_save(sender, instance, *args, **kwargs):
    instance.calculate(save=False)

pre_save.connect(order_pre_save, sender=Order)