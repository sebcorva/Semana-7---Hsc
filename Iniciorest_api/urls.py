from django.urls import path
from . import views

urlpatterns = [
    path('Categoria/', views.lista_categorias, name='lista_categorias'),
    path('Categoria/<id>', views.vista_categoria, name='vista_categoria'),
    path('Producto/', views.lista_productos, name='lista_productos'),
]
