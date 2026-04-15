from django.db import models

# Create your models here.
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food/')
    is_available = models.BooleanField(default=True)
    # <img src="{{ food.image.url }}" class="card-img-top">

    def __str__(self):
        return self.name