from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework.response import Response
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
    return render(request,'products.html',{'data':valores})

def search(request):
    prod_list = Product.objects.all()
    qs = request.GET.get('q')
    
    if qs != '' and qs is not None:
        prod_list = prod_list.filter(title__icontains=qs)
        if len(prod_list) == 0:
            prod_list = {'Não encontramos o item pesquisado'}
    
    paginator = Paginator(prod_list, 15)

    page_number = request.GET.get('page')   
    page_obj = paginator.get_page(page_number)

    return render(request,'search.html',{'page_obj' : page_obj,'paginator': paginator})
