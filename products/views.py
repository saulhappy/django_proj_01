from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("HEY, SAUL!")

def product_detail_view(request, *args, **kwargs):
    qs = Product.objects.all()
    if qs:
        p = qs.first()
        return HttpResponse(f"Product id {p.id}")
    return HttpResponse(f"Nothing to see here, bud :-) ")
    