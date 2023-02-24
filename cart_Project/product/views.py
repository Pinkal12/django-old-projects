from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  ProductSerializer
from .models import Product

# Create your views here.

# API for get the list of all Product in cart: http://127.0.0.1:8000/getproduct/
class ProductView(APIView):
    def get(self, request):
        product_count = Product.objects.all()
        serializer = ProductSerializer(product_count, many=True)
        return Response({'product': serializer.data})
        
        
        