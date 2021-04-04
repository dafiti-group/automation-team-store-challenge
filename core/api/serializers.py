from rest_framework import serializers
from core.models import Produto, CompareProduto, ContadorLoja

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ("id","descricao", "preco_original", "preco_promocional", "promocao", "marca", "loja", "link_produto", "link_img_produto")


class CompareProdutoListSerializer(serializers.ModelSerializer):
    
    produto = ProdutoSerializer(read_only=True)
    
    class Meta:
        model = CompareProduto
        fields = ("id","produto", "preco_produto", "loja", "promocao")        

class CompareProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompareProduto
        fields = ("produto", "preco_produto", "loja", "promocao", "session_key")     

class ComparacaoSerializer(serializers.ModelSerializer):
    
    produto = ProdutoSerializer(read_only=True)
    
    class Meta:
        model = CompareProduto
        fields = ("produto", "preco_produto", "loja", "promocao")           

class PromocaoLojaSerializer(serializers.ModelSerializer):
    quantidade_promo = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Produto
        fields = ("loja","quantidade_promo",)  

class ConcorrenciaLojaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContadorLoja
        fields = ("loja","qtd_vezes",)  


class MarcaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produto
        fields = ("marca",)    


class LojaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produto
        fields = ("loja",)          

