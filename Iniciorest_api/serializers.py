from rest_framework import serializers
from Inicio.models import Categoria, Producto

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['idCategoria', 'nombreCat']

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'especificacionProd', 'stockProd', 'imagenProd', 'tipoprod', 'marca']