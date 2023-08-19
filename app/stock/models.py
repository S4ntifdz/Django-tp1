from django.db import models
from django.contrib.auth.models import AbstractUser
#Duda:
from app.clients.models import ClientModel
# from django.contrib.auth.models import AbstractUser ?

#otra duda, esta app solo se "activaria" cuando el is_seller = True, como y cuando se valida eso?

class BusinessLineChoices(models.TextChoices):
    JARDINERIA = "Jardineria"
    FERRETERIA = "Ferreteria"
    ALMACEN = "Almacen"
    TECNOLOGIA = "Tecnologia"
    OTROS = "Otros"
    
class stock_product(models.Model):
    user = models.ForeignKey(ClientModel)
    business_line = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    quantity = models.IntegerField(max_length=10)
    price = models.FloatField(max_length=10)
    name_product = models.CharField(max_length=140)
    description = models.TextField(max_length=1200)
    code_product = models.IntegerField(max_length=10)
    # picture = 
    expiration = models.DateTimeField()    