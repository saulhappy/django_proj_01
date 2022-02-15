from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

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

    def calculate_tax_totals(self, save=False):
        if not self.product: return {}

        subtotal = self.product.price
        tax_rate = 0.825
        tax_total = round(subtotal*tax_rate, 2)
        total = self.total + tax_total

        totals = {
            "subtotal": subtotal,
            "tax": tax_total,
            "total": total
        }

        for k, v in totals.items():
            setattr(self, k, v)