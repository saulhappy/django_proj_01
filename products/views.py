from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("HEY, SAUL!")

def product_http_detail_view(request, *args, **kwargs):
    qs = Product.objects.all()
    p = qs.first()
    if p:
        return HttpResponse(f"Product id {p.id}")
    return HttpResponse(f"Nothing to see here, bud :-) ")
    
def product_api_detail_view(request, *args, **kwargs):
    qs = Product.objects.all()
    p = qs.first()
    if p:
        return JsonResponse({"id": p.id})
    return JsonResponse({})