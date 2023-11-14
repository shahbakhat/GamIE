from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
# Create your views here.
def checkout(request):
    cart = request.session.get('cart',{})
    if not cart:
        message.error(request,"Youe bag is empty at the moment")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    return render (request, template, context)