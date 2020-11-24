from rest_framework import serializers
from .models import Clothes


class ClothesSerializer(serializers.ModelSerializer):
    """ Class to define Clothes data serializer """
    class Meta:
        model = Clothes
        fields = ("name", "base_price", "final_price", "color",
                  "promotional_campaign", "genre", "collection", "release")
