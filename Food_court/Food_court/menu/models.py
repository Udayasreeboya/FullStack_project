from django.db import models

# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='food/')
    description = models.TextField()

    def __str__(self):
        return self.name