from django.contrib import admin
from stock.models import stock_product
# Register your models here.
#
@admin.register(stock_product)#<--- esto le dice a Django que debe proporcionar una interfaz de administración para el modelo stock_product
class stock_product (admin.ModelAdmin):
    pass
