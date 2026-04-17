from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItem

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=20,default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
