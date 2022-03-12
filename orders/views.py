import pathlib
from mimetypes import guess_type
from tkinter import W
from wsgiref.util import FileWrapper

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from products.models import Product

from .forms import OrderForm
from .models import Order


@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect('/')
    product = qs.first()
    user = request.user
    order_id = request.session.get("order_id")
    order_obj = None
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None
    if not order_id:
        order_obj = Order.objects.create(product=product, user=user)
        request.session['order_id'] = order_obj.id
    form = OrderForm(request.POST or None, product=product, instance=order_obj)
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get("shipping_address")
        order_obj.billing_address = form.cleaned_data.get("billing_address")
        order_obj.mark_paid(save=False)
        order_obj.save()
        del request.session["order_id"]
        return redirect("/success")
    return render(request, 'orders/checkout.html', {"form": form, "object": order_obj})

def download_order_media(request, *args, **kwargs):
    qs = Product.objects.filter(media__isnull=False)
    product_obj = qs.first()

    if not product_obj.media: raise Http404
    
    media_path = product_obj.media.path
    media_path = pathlib.Path(media_path)
    ext = media_path.suffix
    pk = product_obj.pk
    file_name = f"media_{pk}{ext}"

    if not media_path.exists(): raise Http404

    with open(media_path, 'rb') as f:
        wrapper = FileWrapper(f)
        content_type = 'application/force-download'
        guessed_media_type = guess_type(media_path)[0]
        if guessed_media_type:
            content_type = guessed_media_type
        response =  HttpResponse(wrapper, content_type=content_type)
        response['Content-Disposition'] = f"attachment;filename={file_name}"
        response['X-SendFile'] = f"{file_name}"

    return response