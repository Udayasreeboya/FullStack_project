from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FoodItem

def menu_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'menu/menu.html', {'foods': foods})