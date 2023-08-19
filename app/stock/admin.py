from django.contrib import admin
from stock.models import stock_product
# Register your models here.

#COMO VOLETIE EL MODELO DE USER QUE USA X DEFAULT DJANGO PARA VALIDAR TAMBIEN INDIRECTAMENTE VOLETIE EL ADMIN
#TENGO QUE CREAR UNO ASOCIADO AL MODELO DE USER QUE ASIGNE (EN ESTE CASO CLIENTS)

@admin.register(stock_product)
class stock_product (admin.ModelAdmin):
    pass
