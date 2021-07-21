from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Shoes
from .serializers import ShoesSerializer


class ShoesViewSet(ModelViewSet):
    serializer_class = ShoesSerializer
    queryset = Shoes.objects.all().order_by("-data_de_lancamento")
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ShoesSerializer(queryset, many=True)
        return Response(serializer.data)