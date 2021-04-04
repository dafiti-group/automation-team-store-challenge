from django_filters import rest_framework as filters
from core.models import Produto, CompareProduto

class ProdutoFilterSet(filters.FilterSet):
    descricao = filters.CharFilter(
        field_name="descricao", lookup_expr="icontains"
    )
    
    loja = filters.CharFilter(
        field_name="loja", lookup_expr="icontains"
    )

    marca = filters.CharFilter(
        field_name="marca", lookup_expr="icontains"
    )

    #menor
    preco_menor = filters.NumberFilter(
        field_name="preco_original", lookup_expr='gte'
    )

    #maior
    preco_maior = filters.NumberFilter(
        field_name="preco_original", lookup_expr='lte'
    )

    #menor
    preco_promo_menor = filters.NumberFilter(
        field_name="preco_promocional", lookup_expr='gte'
    )

    #maior
    preco__promo_maior = filters.NumberFilter(
        field_name="preco_promocional", lookup_expr='lte'
    )
    class Meta:
        model = Produto
        fields = ["descricao", "loja", "preco_original", "preco_menor", "preco_maior", "preco_promo_menor", "preco__promo_maior", "marca"]
        
class CompareProdutoFilterSet(filters.FilterSet):
    produto = filters.CharFilter(
        field_name="produto__descricao", lookup_expr="icontains"
    )
    
    loja = filters.CharFilter(
        field_name="loja", lookup_expr="icontains"
    )
    class Meta:
        model = CompareProduto
        fields = ["produto", "loja", "promocao"]        