from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class ProductCategory(models.Model):
    MARKETING_ANALYTICS = 'marketing_analytics'
    SALES_ANALYTICS = 'sales_analytics'
    ENGINEERING_ANALYTICS = 'engineering_analytics'
    WEB_ANALYTICS = 'web_analytics'

    CATEGORY_CHOICES = (
        (MARKETING_ANALYTICS, 'Marketing Analytics'),
        (SALES_ANALYTICS, 'Sales Analytics'),
        (ENGINEERING_ANALYTICS, 'Engineering Analytics'),
        (WEB_ANALYTICS, 'Web Analytics')
    )

    category_name = models.CharField(max_length=140, choices=CATEGORY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.category_name

class Product(ProductCategory):
    def get_or_create_default_category():
        obj, created = ProductCategory.objects.get_or_create(category_name='marketing_analytics')
        return obj

    CATEGORY2_CHOICES = (
        ('Marketing Analytics', 'Marketing Analytics'),
        ('Sales Analytics', 'Sales Analytics'),
        ('Engineering Analytics', 'Engineering Analytics'),
        ('Web Analytics', 'Web Analytics')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=140)
    price = models.IntegerField(default=0)
    slogan = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_category', default=get_or_create_default_category)
    category2 = models.CharField(max_length=140, choices=CATEGORY2_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product_name