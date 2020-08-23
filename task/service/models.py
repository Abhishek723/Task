from django.db import models
from django.utils import timezone

# Create your models here.


class Restaurent(models.Model):
    name = models.CharField(max_length = 200)
    discription = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length = 200) 
    address = models.TextField(max_length=500)
    restaurent = models.ForeignKey(Restaurent, on_delete=models.CASCADE)
    pincode = models.CharField(max_length = 6)
    # branchOwner = models.OneToOneField(BranchOwner, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Order(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    foodItem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    order_time = models.DateTimeField(default=timezone.now)

class OrderDiscription(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    orderItem = models.IntegerField()
    orderQuantity = models.IntegerField()