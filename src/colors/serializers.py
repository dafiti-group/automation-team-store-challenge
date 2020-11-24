from rest_framework import serializers
from .models import Color


class ColorSerializer(serializers.ModelSerializer):
    """ Class to define Color data serializer """
    class Meta:
        model = Color
        fields = ("name", "hex_code",)
