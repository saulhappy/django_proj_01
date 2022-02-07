from tkinter import W

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.models import Product

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
    return render(request, 'forms.html', {})