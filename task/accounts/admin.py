from django.contrib import admin
from accounts.models import Customer,BranchOwner
# Register your models here.

admin.site.register(Customer)
admin.site.register(BranchOwner)

