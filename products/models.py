from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class ProductCategory(models.Model):
    CATEGORY_NAME_CHOICES = (
        ('Candy', 'Candy'),
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
    category_name = models.CharField(max_length=140, choices=ProductCategory.CATEGORY_NAME_CHOICES, null=True, blank=True)
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def has_inventory(self):
        return self.inventory > 0

    def decrement_inventory(self, save=True):
        self.inventory -= 1
        if save: self.save()
        return self.inventory

    def __str__(self):
        return self.product_name
