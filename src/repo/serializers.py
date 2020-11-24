""" Module to define Class responsible for generic errors serializer """

from rest_framework import serializers


# pylint: disable=abstract-method
class ErrorSerializer(serializers.Serializer):
    """ Class responsible for generic errors serializer """
    field_name_wrong = serializers.ListField()
