from django.db.models import fields
from rest_framework import serializers
from .models import Product, ProductCategory, Brand

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ['pk', 'name', 'description']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['pk', 'name', 'logo']


class ProductSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())
    product_type = serializers.ChoiceField(choices=Product.TYPES)
    gender = serializers.ChoiceField(choices=Product.GENDERS)
    size = serializers.ChoiceField(choices=Product.SIZES)
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    color = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    brand_name = serializers.StringRelatedField(source='brand', read_only=True)
    product_type_name = serializers.ChoiceField(choices=Product.TYPES, source='get_product_type_display', read_only=True)
    gender_name = serializers.ChoiceField(choices=Product.GENDERS, source='get_gender_display', read_only=True)
    size_name = serializers.ChoiceField(choices=Product.SIZES, source='get_size_display', read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.size = validated_data.get('size', instance.size)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.color = validated_data.get('color', instance.color)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = [
            'pk', 'name', 'category', 'product_type', 'gender', 'size', 'brand', 'color', 'price', 
            'category_name', 'brand_name', 'product_type_name', 'gender_name', 'size_name'
            ]

