from .models import WomenShoes
from .serializers import WomenShoesSerializer
from rest_framework import generics


class WomenShoesList(generics.ListCreateAPIView):
    queryset = WomenShoes.objects.all()
    serializer_class = WomenShoesSerializer


class WomenShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WomenShoes.objects.all()
    serializer_class = WomenShoesSerializer
