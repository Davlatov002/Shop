from django.shortcuts import render
from .models import Praduct, Category
from .serialazer import PraductSerialazer, CategorySerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categorys(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categorys_get_id(request, pk):
    if request.method == 'GET':
        categorys = Category.objects.get(id=pk)
        serializer = CategorySerializer(categorys)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praducts(request):
    if request.method == 'GET':
        praducts = Praduct.objects.all()
        serializer = PraductSerialazer(praducts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praduct_get_id(request, pk):
    if request.method == 'GET':
        praduct = Praduct.objects.get(id=pk)
        serializer = PraductSerialazer(praduct)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


