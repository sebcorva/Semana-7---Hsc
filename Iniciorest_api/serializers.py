from rest_framework import serializers
from Inicio.models import Categoria, Producto, Marca, TipoProd

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['idCategoria', 'nombreCat']

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'especificacionProd', 'stockProd', 'imagenProd', 'tipoprod', 'marca']

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Marca
        fields = ['idMarca', 'nombreMarca']

class TipoProdSerializers(serializers.ModelSerializer):
    class Meta:
        model=TipoProd
        fields = ['idTiporod', 'nombreTipoProd']