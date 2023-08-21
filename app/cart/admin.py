from django.contrib import admin
from cart.models import CartModel
# Register your models here.

@admin.register(CartModel)
class CartModel (admin.ModelAdmin):
    pass
