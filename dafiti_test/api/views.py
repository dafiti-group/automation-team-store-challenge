from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .models import Product
from .serializers import ProductSerializer
import requests, json

# Create your views here.

class product_list(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     products = Product.objects.filter(title__icontains='azul')
    #     serializer = ProductSerializer(products, many=True)
    #     print(request.data) 
    #     return Response(serializer.data)

def mainPage(request):
    valores = requests.get('http://localhost:8000/api').json()
    data = {}
    return render(request,'products.html',{'data':valores})