from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.

def test_view(request, *args, **kwargs):
    import pdb; pdb.set_trace()
    return HttpResponse("This is the test view")

def home_view(request, *args, **kwargs):
    # return HttpResponse("HEY, SAUL!")
    query = request.GET.get('q')
    qs = Product.objects.filter(description__icontains=query[0])
    print(query, qs)
    context = {"name": "Saul"}
    return render(request, "home.html", context)

def product_http_detail_view(request, id):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id: {p.id}")
    return render(request, "products/detail.html", {"object": p})

def product_api_detail_view(request, id):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found."})
    return HttpResponse(f"Product id: {p.id}")

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)   
    if form.is_valid():
        data = form.cleaned_data
        Product.objects.create(**data)

    return render(request, "form.html", {"form": form})