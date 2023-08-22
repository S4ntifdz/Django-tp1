from django import forms
from django.contrib.auth.models import AbstractUser
from clients.models import ClientModel
class SignUpForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = ClientModel
        fields =['cuit','business_line','business_line_interes','state','city','postal_code','phone_number','avatar']