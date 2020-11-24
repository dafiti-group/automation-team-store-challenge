from rest_framework import serializers
from .models import PromotionalCampaign


class PromotionalCampaignSerializer(serializers.ModelSerializer):
    """ Class to define PromotionalCapaign data serializer """
    class Meta:
        model = PromotionalCampaign
        fields = ("name", "percentage_discount",)
