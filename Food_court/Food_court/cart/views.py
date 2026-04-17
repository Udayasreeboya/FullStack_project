from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from menu.models import FoodItem


@login_required(login_url='login')
def add_to_cart(request, id):

    food = FoodItem.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        food_item=food
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required(login_url='login')
def cart_view(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        item.total = item.food_item.price * item.quantity
        total += item.total

    return render(request, 'auth/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required(login_url='login')
def increase_qty(request, id):

    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.save()

    return redirect('cart')


@login_required(login_url='login')
def decrease_qty(request, id):

    cart = Cart.objects.get(id=id)

    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()

    return redirect('cart')


@login_required(login_url='login')
def remove_item(request, id):

    cart = Cart.objects.get(id=id)
    cart.delete()

    return redirect('cart')