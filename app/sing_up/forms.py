# from django import forms
# from django.contrib.auth.models import AbstractUser
# from clients.models import ClientModel
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = AbstractUser
#         fields = ['first_name', 'last_name', 'username','password']

# class SignUpForm(UserForm, forms.ModelForm):
#     class Meta:
#         model = ClientModel
#         fields = ['first_name', 'last_name', 'username','password','cuit', 'business_line', 'business_line_interes', 'state', 'city', 'postal_code', 'phone_number', 'avatar']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from clients.models import ClientModel

class SignUpStep1Form(UserCreationForm):
    class Meta:
        model = ClientModel
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    username = forms.CharField(
        label="Username",
        max_length=150,  # Establece la longitud máxima deseada
        help_text='',  # Borra la ayuda que se muestra debajo del campo
    )
    password1 = forms.CharField(
        label="Password",
        max_length=150,  # Establece la longitud máxima deseada
        help_text='',  # Borra la ayuda que se muestra debajo del campo
    )
    password2 = forms.CharField(
        label="Repeat password",
        max_length=150,  # Establece la longitud máxima deseada
        help_text='',  # Borra la ayuda que se muestra debajo del campo
    )
class SignUpStep2Form(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ['cuit', 'business_line', 'business_line_interes', 'state', 'city', 'postal_code', 'phone_number', 'avatar']
