#Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#local
from .models import Products, Category, File
from .serializer import *

#Rest Framework
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response


class ProductListView(APIView):
    def get(self, request):
        posts = Products.objects.all()
        serialized = ProductsSerializer(
            posts, many=True, context={'request': request})
        return Response(serialized.data)


class ProductDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        post = get_object_or_404(Products,pk=pk)
        serialized = ProductsSerializer(post,context={'request':request})
        return Response(serialized.data)
    

class CategorylistView(APIView):
    
    def get(self,request):
        posts = Category.objects.all()
        serialized = CategorySerializer(posts,many=True,context={'request':request})
        return Response(serialized.data)
    
    
class CategoryDetailView(APIView):
    def get(self,request,pk):
        post = get_object_or_404(Category,pk=pk)
        serialized = CategorySerializer(post,context={'request':request})
        return Response(serialized.data)
    
class FileListView(APIView):
    def get(self,request,product_pk):
        posts = File.objects.filter(product_id = product_pk)
        serialized = FileSerializer(posts,many= True,context={'request':request})
        return Response(serialized.data)
    
class FileDetailView(APIView):
    def get(self,request,product_pk,pk):
        try:
            f = File.objects.get(pk=pk,product_id = product_pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized =FileSerializer(f,context={'request':request})
        return Response(serialized.data)
    
    
    
    
