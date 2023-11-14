from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that renders cart page """

    return render(request, 'cart/cart.html')