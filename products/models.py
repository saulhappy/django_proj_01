from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class ProductCategory(models.Model):
    CATEGORY_NAME_CHOICES = (
        ('Marketing Analytics', 'Marketing Analytics'),
        ('Sales Analytics', 'Sales Analytics'),
        ('Engineering Analytics', 'Engineering Analytics'),
        ('Web Analytics', 'Web Analytics'),
        ('Cereal', 'Cereal')
    )

    name = models.CharField(max_length=140, choices=CATEGORY_NAME_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(ProductCategory):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    slogan = models.TextField(null=True, blank=True)
    category_name = models.CharField(max_length=140, choices=ProductCategory.CATEGORY_NAME_CHOICES, null=True, blank=True, default='Cereal')
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def has_inventory(self):
        return self.inventory > 0

    def __str__(self):
        return self.product_name

    def calculate_tax_totals(self, save=False):
        if not self.product: return {}

        subtotal = self.product.price
        tax_rate = 0.825
        tax_total = round(subtotal*tax_rate, 2)
        total = None

        totals = {
            "subtotal": subtotal,
            "tax": tax_total,
            "total": total
        }

        for k, v in totals.items():
            setattr(self, k, v)

