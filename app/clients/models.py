from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class BusinessLineChoices(models.TextChoices):
    JARDINERIA = "Jardineria"
    FERRETERIA = "Ferreteria"
    ALMACEN = "Almacen"
    TECNOLOGIA = "Tecnologia"
    OTROS = "Otros"
    
class ClientModel(AbstractUser):
    cuit = models.CharField(max_length=11)
    business_line = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    business_line_interes = models.CharField(choices=BusinessLineChoices.choices, max_length=128, default=BusinessLineChoices.OTROS.value)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    state = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.CharField(max_length = 4)
    phone_number = models.CharField(max_length = 64)
    avatar = models.ImageField(upload_to="avatar", null = True)