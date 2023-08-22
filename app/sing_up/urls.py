from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs existentes
    path('signup/', views.signup_view, name='signup'),
]