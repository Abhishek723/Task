from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth.models import User
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
from accounts.models import BranchOwner

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def UpdateFoodItem(request,id):

    try:
        instance = FoodItem.objects.get(id = id)
    except FoodItem.DoesNotExist as e:
        return JsonResponse({"error":"Given Food Item is not found"},status = 404)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        currentUser = request.user
        try:
            BranchOwner.objects.get(user_id = currentUser)
        except BranchOwner.DoesNotExist as e:
            return JsonResponse({"error":"User is not BranchOwner"},status = 403)
        finalQuantity = data['quantity']
        serializer = FoodItemSerializer(instance,data = {"quantity":finalQuantity},partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 200)
        else:
            return JsonResponse(serializer.errors,status = 400)
        




