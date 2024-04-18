from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from Inicio.models import Categoria, Producto, Marca, TipoProd
from .serializers import CategoriaSerializers, ProductoSerializers, MarcaSerializers, TipoProdSerializers
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

# Create your views here.

#api categorias
@csrf_exempt
@api_view(('GET', 'POST'))
def lista_categorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
@permission_classes((IsAuthenticated,))
def vista_categoria(request, id):
    try:
        categoria = Categoria.objects.get(idCategoria=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializers(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CategoriaSerializers(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#api productos        
        
@csrf_exempt
@api_view(('GET', 'POST'))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializers(productos, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_productos(request, id):
	try:
		productos = Producto.objects.get(pk=id)
	except Producto.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = ProductoSerializers(productos)
		return Response(serializer.data)
	elif request.method == 'PUT' or request.method == 'PATCH':
		data = JSONParser().parse(request)
		serializer = ProductoSerializers(productos,data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		productos.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

#api marcas

@csrf_exempt
@api_view(['GET','POST'])
def lista_marcas(request):
	if request.method == 'GET':
		marcas = Marca.objects.all()
		serializer = MarcaSerializers(marcas, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MarcaSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		else:
			print('error', serializer.errors)
			return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
			
@api_view(['GET','PUT','PATCH','DELETE'])
def vista_marcas(request, id):
	try:
		marcas = Marca.objects.get(pk=id)
	except Marca.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = MarcaSerializers(marcas)
		return Response(serializer.data)
	elif request.method == 'PUT' or request.method == 'PATCH':
		data = JSONParser().parse(request)
		serializer = MarcaSerializers(marcas,data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		marcas.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

#api tipo productos

@csrf_exempt
@api_view(['GET','POST'])
def lista_tipos_productos(request):
	if request.method == 'GET':
		tipos_productos = TipoProd.objects.all()
		serializer = TipoProdSerializers(tipos_productos, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TipoProdSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		else:
			print('error', serializer.errors)
			return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
			
@api_view(['GET','PUT','PATCH','DELETE'])
def vista_tipos_productos(request, id):
	try:
		tipos_productos = TipoProd.objects.get(pk=id)
	except TipoProd.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = TipoProdSerializers(tipos_productos)
		return Response(serializer.data)
	elif request.method == 'PUT' or request.method == 'PATCH':
		data = JSONParser().parse(request)
		serializer = TipoProdSerializers(tipos_productos,data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		tipos_productos.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)