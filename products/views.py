from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.shortcuts import render

from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("HEY, SAUL!")

def product_http_detail_view(request, id):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"Product id: {p.id}")
    
def product_api_detail_view(request, id):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found."})
    return HttpResponse(f"Product id: {p.id}")