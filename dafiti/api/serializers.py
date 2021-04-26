from django.utils.text import slugify
from rest_framework import serializers

from dafiti.core.models import Produto, Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'slug', 'nome')

    def update(self, instance, validated_data):
        try:
            nome = validated_data.get('nome')
            instance.nome = nome
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(e.args)

    def create(self, validated_data):
        try:
            nome_slug = slugify(validated_data.get('nome'))
            marca = Marca.objects.filter(slug=nome_slug).first()
            if marca:
                return self.update(marca, validated_data)
            else:
                marca = Marca()
                return self.update(marca, validated_data)
        except Exception as e:
            raise serializers.ValidationError(e.args)


class ProdutoSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(default='')

    class Meta:
        model = Produto
        fields = ('id',
                  'nome',
                  'sku',
                  'descricao',
                  'quantidade',
                  'preco',
                  'tipo',
                  'marca',
                  'total_estoque')

    def update(self, instance, validated_data):
        try:
            instance.nome = validated_data.get('nome', instance.nome)
            instance.sku = validated_data.get('sku', instance.sku)
            instance.descricao = validated_data.get('descricao', instance.descricao)
            instance.quantidade = validated_data.get('quantidade', instance.quantidade)
            instance.preco = validated_data.get('preco', instance.preco)
            instance.tipo = validated_data.get('tipo', instance.tipo)
            instance.marca = Marca.objects.filter(slug=slugify(validated_data.get('marca'))).first()
            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(e.args)

    def create(self, validated_data):
        try:
            sku = validated_data.get('sku')
            produto = Produto.objects.filter(sku=sku).first()
            if produto:
                retorno = self.update(produto, validated_data)
            else:
                produto = Produto()
                retorno = self.update(produto, validated_data)
            return retorno
        except Exception as e:
            raise serializers.ValidationError(e.args)
