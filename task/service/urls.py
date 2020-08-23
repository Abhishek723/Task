from django.contrib import admin
from django.urls import path,include
from service.views import placeOrder
urlpatterns = [
    path('',placeOrder)
]
