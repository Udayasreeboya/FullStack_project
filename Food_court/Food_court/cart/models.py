from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from menu.models import FoodItem

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)