from .models import WomenShoes
from rest_framework import serializers
import datetime


class WomenShoesSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(required=False, allow_blank=True, max_length=50)
    colors = serializers.CharField(max_length=50)
    count = serializers.IntegerField(required=False)
    dateAdded = serializers.DateTimeField(initial=datetime.date.today)
    dateUpdated = serializers.DateTimeField(initial=datetime.date.today)
    manufacturer = serializers.CharField(required=False, allow_blank=True, max_length=50)
    name = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    weight = serializers.DecimalField(max_digits=9, decimal_places=2)

    def create(self, validated_data):
        """
        Create and return a new `WomenShoes` instance, given the validated data.
        """
        return WomenShoes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `WomenShoes` instance, given the validated data.
        """
        instance.brand = validated_data.get('brand', instance.brand)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.colors = validated_data.get('colors', instance.colors)
        instance.count = validated_data.get('count', instance.count)
        instance.dateAdded = validated_data.get('dateAdded', instance.dateAdded)
        instance.dateUpdated = validated_data.get('dateUpdated', instance.dateUpdated)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance

    class Meta:
        model = WomenShoes
        fields = [
            'id',
            'brand',
            'colors',
            'count',
            'dateAdded',
            'dateUpdated',
            'manufacturer',
            'name',
            'price',
            'weight'
        ]
