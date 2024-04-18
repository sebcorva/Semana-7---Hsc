from django.urls import path
from . import views

#api/
urlpatterns = [
    path('categoria/', views.lista_categorias, name='lista_categorias'),
    path('categoria/<id>', views.vista_categoria, name='vista_categoria'),
    path('producto/', views.lista_productos, name='lista_productos'),
    path('producto/<id>', views.vista_productos, name="vista_productos"),
    path('marca/', views.lista_marcas, name="lista_marcas"),
	path('marca/<id>', views.vista_marcas, name="vista_marcas"),
    path('tipo-producto/', views.lista_tipos_productos, name="lista_tipo_productos"),
	path('tipo-producto/<id>', views.vista_tipos_productos, name="vista_tipo_productos"),
]
