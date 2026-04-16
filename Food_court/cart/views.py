from django.shortcuts import render, redirect, get_object_or_404
from menu.models import FoodItem
from .models import Cart
from django.contrib.auth.decorators import login_required

@login_required
# def add_to_cart(request):
# @login_required
# def add_to_cart(request):

def add_to_cart(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        food_item=food
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.delete()
    return redirect('cart')