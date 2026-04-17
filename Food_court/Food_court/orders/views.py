from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect,render
from cart.models import Cart
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            food_item=item.food_item,
            quantity=item.quantity,
            total_price=item.food_item.price * item.quantity
        )

    cart_items.delete()

    return redirect('orders')


@login_required(login_url='login')
def order_history(request):

    orders = Order.objects.filter(user=request.user)

    return render(request,'auth/orders.html',{
        'orders':orders
    })