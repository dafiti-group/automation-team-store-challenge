from rest_framework import viewsets, authentication, permissions

from dafiti.api.mixins import CreateListMixin
from dafiti.api.serializers import ProdutoSerializer, MarcaSerializer
from dafiti.core.models import Produto


class MarcaViewSet(CreateListMixin, viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Produto.objects.all()
    http_method_names = ['get', 'post', 'head']
    serializer_class = MarcaSerializer


class ProdutoViewSet(CreateListMixin, viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Produto.objects.all()
    http_method_names = ['get', 'post', 'head']
    serializer_class = ProdutoSerializer
