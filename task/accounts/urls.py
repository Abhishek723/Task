from django.contrib import admin
from django.urls import path,include
from accounts.views import UpdateFoodItem
urlpatterns = [
    path('update/fooditems/<int:id>/edit',UpdateFoodItem)
]
