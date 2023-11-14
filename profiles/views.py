from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    A view to display and handle the user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')  # noqa
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    A view to display a past order confirmation for a specific order number.
    """
    order = get_object_or_404(Order, order_number=order_number)

    if order.user_profile.user != request.user:
        messages.warning(request, 'You can only view your own order history!')
        return render(request, '403.html')
    else:
        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        ))

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

    return render(request, template, context)