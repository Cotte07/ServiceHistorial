from django.contrib import admin 
from django.urls import path, include
from .views import  historial_productos_view

urlpatterns = [
    path('historial/', historial_productos_view, name='historial')
]