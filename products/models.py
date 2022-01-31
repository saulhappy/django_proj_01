from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class DataConnectorCateogry(models.Model):
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

    title = models.CharField(max_length=140, choices=CATEGORY_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.title

class Product(DataConnectorCateogry):
    def get_default_category(self):
        return DataConnectorCateogry.objects.get(name="marketing_analytics")
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=140)
    price = models.IntegerField(default=0)
    slogan = models.TextField(null=True, blank=True)
    category = models.ForeignKey(DataConnectorCateogry, default=get_default_category, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_category')

    def __str__(self) -> str:
        return self.name