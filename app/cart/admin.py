from django.contrib import admin
from cart.models import CartModel
from cart.models import Cart_fath
# Register your models here.

@admin.register(CartModel)
class CartModel (admin.ModelAdmin):
    pass
# @admin.register(Cart_fath)
# class Cart_fath (admin.ModelAdmin):
#     pass

    
from django.contrib import admin
from .models import Cart_fath

@admin.register(Cart_fath)
class Cart_fathAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Limpia el carrito actual antes de cambiar al nuevo usuario.
        cart_instance = Cart_fath.objects.get(pk=object_id)
        cart_instance.items.clear()
        return super().change_view(request, object_id, form_url, extra_context)