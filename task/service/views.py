from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import serializers
from service.models import (
    Restaurent,
    Branch, 
    FoodItem, 
    Order, 
    OrderDiscription
    )

from service.serializers import (
    FoodItemSerializer,
    RestaurentSerializer, 
    BranchSerializer, 
    )

from django.views.decorators.csrf import csrf_exempt


# # Create your views here.

@csrf_exempt
def placeOrder(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        orderedBranch = data['branchId']
        #print(orderedBranch)
        for orderItem in data['orderList']:
            
            orderFoodItem = orderItem['orderFoodItemId']
            orderQuantity = orderItem['quantity']
            print("orderFoodItem",orderFoodItem)
            print("orderQuantity",orderQuantity)
            try:
                instance = FoodItem.objects.filter(branch_id=orderedBranch, id=orderFoodItem)
            except FoodItem.DoesNotExist as e:
                return JsonResponse({'error':'Given fooditem not found'},status = 404)
            print("instance[0].quantity",instance[0].quantity)
            if instance[0].quantity < orderQuantity:
                return JsonResponse({'error':'Given fooditem not found'},status = 404)
        
        for orderItem in data['orderList']:
            print("orderFoodItem",orderFoodItem)
            print("orderQuantity",orderQuantity)
            orderFoodItem = orderItem['orderFoodItemId']
            orderQuantity = orderItem['quantity']
            # instance = FoodItem.objects.filter(branch_id=orderedBranch, id=orderFoodItem)
            instance = FoodItem.objects.all()
            instanceSerializer = FoodItemSerializer(instance,many = True)
            instance[0].quantity = instance[0].quantity - orderQuantity
            print("instance[0].quantity",instanceSerializer.data)

            serializer = FoodItemSerializer(data = instance)

            if serializer.is_valid():
                serializer.save()
            else:
                return JsonResponse(serializer.errors,status = 400)
        

