from django.db import models
from clients.models import ClientModel
from stock.models import stock_product
# Create your models here.
# DUDA: Para la cantidad del carrito de compras, tengo que extender la clase productos?
# si ese es el caso, a que clase conecto como fk

class product_with_qt(stock_product, models.Model):
    name_product 
    quantity = models.IntegerField()

class CartModel (models.Model):
    user = models.ForeignKey(ClientModel,on_delete=models.CASCADE)
    products = models.ForeignKey(stock_product,on_delete=models.CASCADE)