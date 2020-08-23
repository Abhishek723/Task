from rest_framework import serializers
from service.models import (
    Restaurent,
    Branch, 
    FoodItem, 
    Order, 
    OrderDiscription
    )


class FoodItemSerializer(serializers.ModelSerializer):
    branch = serializers.CharField(source = "branch.name",read_only= True)

    class Meta:
        model = FoodItem
        fields = ('id',
                  'name',
                  'price',
                  'quantity',
                  'branch'
                )

class RestaurentSerializer(serializers.ModelSerializer):
    branches = FoodItemSerializer(many=True)
    class Meta:
        model = Restaurent
        fields = ('name',
                  'discription',
                  'branches'
                )


class BranchSerializer(serializers.ModelSerializer):
    foodItems = FoodItemSerializer(many=True)
    restaurent = serializers.CharField(source = "restaurent.name",read_only= True)
    class Meta:
        model = Branch
        fields = ('id',
                  'name',
                  'address',
                  'pincode',
                  'foodItems',
                  'restaurent'
                )

