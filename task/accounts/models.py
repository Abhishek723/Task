from django.db import models
from django.contrib.auth.models import User

from service.models import Branch
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length = 10) 

class BranchOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length = 10) 
