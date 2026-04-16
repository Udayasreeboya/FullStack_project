from django.shortcuts import render, redirect, get_object_or_404
from menu.models import FoodItem
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.http import JsonResponse

# def add_to_cart(request, id):
#     if not request.user.is_authenticated:
#         return JsonResponse({"error": "Please login first"})

    # your cart logic
# def add_to_cart(request):
# @login_required
# def add_to_cart(request):


@login_required(login_url='/admin/login/')
def add_to_cart(request, food_id):
    food = FoodItem.objects.get(id=food_id)

    Cart.objects.create(
        user=request.user,
        food_item=food,
        quantity=1
    )

    return JsonResponse({"message": "Added to cart"})


# def add_to_cart(request, food_id):
#     if not request.user.is_authenticated:
#         return JsonResponse({"message": "Login required"}, status=401)

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