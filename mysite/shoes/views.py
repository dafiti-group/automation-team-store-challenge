from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Shoes
from .serializers import ShoesSerializer


class ShoesViewSet(ModelViewSet):
    serializer_class = ShoesSerializer
    queryset = Shoes.objects.all().order_by("-data_de_lancamento")
    pagination_class = PageNumberPagination