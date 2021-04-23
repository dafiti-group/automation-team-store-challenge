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
            marca, _ = Marca.objects.get_or_create(slug=nome_slug)
            return self.update(marca, validated_data)
        except Exception as e:
            raise serializers.ValidationError(e.args)


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('nome',
                  'sku',
                  'descricao',
                  'quantidade',
                  'preco',
                  'tipo',
                  'marca')

    def update(self, instance, validated_data):
        try:
            instance.nome = validated_data.get('nome', instance.nome)
            instance.sku = validated_data.get('sku', instance.sku)
            instance.descricao = validated_data.get('descricao', instance.descricao)
            instance.quantidade = validated_data.get('quantidade', instance.quantidade)
            instance.preco = validated_data.get('preco', instance.preco)
            instance.tipo = validated_data.get('tipo', instance.tipo)
            instance.marca = Marca.objects.get(slug=slugify(validated_data.get('marca')))
            instance.save()
        except Exception as e:
            raise serializers.ValidationError(e.args)

    def create(self, validated_data):
        try:
            sku = validated_data.get('sku')
            produto, _ = Produto.objects.get_or_create(sku=sku)
            self.update(produto, validated_data)
            return produto
        except Exception as e:
            raise serializers.ValidationError(e.args)
