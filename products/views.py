from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, ProductCategory
from .serializers import *

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        products = Product.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = ProductSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({
            'data':serializer.data, 
            'count': paginator.count,
            'perpage': paginator.per_page,
            'numpages':paginator.num_pages, 
            'nextlink':'/api/products/?page='+str(nextPage),
            'prevlink':'/api/products/?page='+str(previousPage),
            })

    elif request.method == 'POST':
        data = request.data

        if data['category_obj']:
            cat_serializer = ProductCategorySerializer(data=data['category_obj'])
            if cat_serializer.is_valid():
                cat_serializer.save()
                data['category'] = cat_serializer.data['pk']
        
        if data['brand_obj']:
            bran_serializer = BrandSerializer(data=data['brand_obj'])
            if bran_serializer.is_valid():
                bran_serializer.save()
                data['brand'] = bran_serializer.data['pk']

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status.status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':

        data = request.data

        if data['category_obj']:
            cat_serializer = ProductCategorySerializer(data=data['category_obj'])
            if cat_serializer.is_valid():
                cat_serializer.save()
                data['category'] = cat_serializer.data['pk']
        
        if data['brand_obj']:
            bran_serializer = BrandSerializer(data=data['brand_obj'])
            if bran_serializer.is_valid():
                bran_serializer.save()
                data['brand'] = bran_serializer.data['pk']

        serializer = ProductSerializer(product, data=data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def brands_list(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)

