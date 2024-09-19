from django.urls import path

from .views import index, contato

# Recebe as requisições de rotas do django
urlpatterns = [
    path('', index),
    path('contato', contato),
]