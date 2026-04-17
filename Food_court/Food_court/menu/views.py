from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FoodItem

def menu_list(request):

    items = FoodItem.objects.all()

    return render(request,'auth/menu.html',{
        'items':items
    })