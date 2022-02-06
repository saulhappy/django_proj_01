from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

# Create your models here.

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)