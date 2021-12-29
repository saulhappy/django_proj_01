from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=140)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)