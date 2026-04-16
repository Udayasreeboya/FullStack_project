from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import redirect
from cart.models import Cart
from .models import Order, OrderItem
@login_required

def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items:
        return redirect('cart')

    total = sum(item.total_price() for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            food_item=item.food_item,
            quantity=item.quantity,
            price=item.food_item.price
        )

    cart_items.delete()  # clear cart

    return redirect('my_orders')


from django.shortcuts import render
from .models import Order

# def my_orders(request):
#     orders = Order.objects.filter(user=request.user).order_by('-created_at')

#     return render(request, 'orders/orders.html', {
#         'orders': orders
#     })
from django.http import JsonResponse
from .models import Order

# def my_orders(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({"error": "Please login first"})

#     orders = Order.objects.filter(user=request.user)
@login_required(login_url='/auth/login/')
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return JsonResponse(list(orders.values()), safe=False)