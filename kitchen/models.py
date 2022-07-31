from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return f'{self.name} category'

class Food(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='foods')
    
class Kitchen(models.Model):
    foods = models.ManyToManyField('Food', related_name='kitchen_offered')
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField()
    
    
    @property
    def available_foods(self):
        return self.objects.foods.filter(quantity__gte = 1)
    
    @property
    def waiting_order(self):
        return self.objects.ordered.filter(delivered = False)

class Ordered(models.Model):
    customer = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=25)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    delivered = models.BooleanField(default=False)
    delivery_point = models.TextField()
    kitchen = models.ForeignKey(Kitchen, on_delete=models.SET_NULL, null=True)
    