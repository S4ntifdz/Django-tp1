# from django.db import models
# from clients.models import ClientModel
# from stock.models import stock_product
# # Create your models here.
# # DUDA: Para la cantidad del carrito de compras, tengo que extender la clase productos?
# # si ese es el caso, a que clase conecto como fk

# # validaciones en donde

# # class product_with_qt(stock_product, models.Model):
# #     name = stock_product.name_product
# #     quantity = models.IntegerField()

# class CartModel (models.Model):
#    # user = models.ForeignKey(ClientModel,on_delete=models.CASCADE)
#     products = models.ForeignKey(stock_product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
    
#     def __str__(self): 
#         return f"{self.products} | cantidad: {self.quantity}"

# class Cart_fath(models.Model):
#     super(CartModel)
#     user = models.ForeignKey(ClientModel,on_delete=models.CASCADE)

from django.db import models
from clients.models import ClientModel
from stock.models import stock_product

class CartModel(models.Model):
    #user = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ForeignKey(stock_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.products} | Cantidad: {self.quantity}"

class Cart_fath(models.Model):
    user = models.OneToOneField(ClientModel, on_delete=models.CASCADE)  # Cambiamos a OneToOneField para garantizar que cada usuario tenga un solo carrito.
    items = models.ManyToManyField(CartModel)

    def __str__(self):
        return f"Carrito de {self.user}"

    

