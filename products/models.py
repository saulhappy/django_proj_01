from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=140)
    price = models.IntegerField(default=0)
    slogan = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name