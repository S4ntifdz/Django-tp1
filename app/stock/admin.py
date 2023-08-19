from django.contrib import admin
from stock.models import stock_product
# Register your models here.


@admin.register(stock_product)
class stock_product (admin.ModelAdmin):
    pass
