from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.lista_categorias, name='lista_categorias'),
    path('categoria/<id>', views.vista_categoria, name='vista_categoria'),
    path('producto/', views.lista_productos, name='lista_productos'),
    path('producto/<id>', views.vista_productos, name="vista_productos"),
]
