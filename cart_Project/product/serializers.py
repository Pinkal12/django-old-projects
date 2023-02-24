from dataclasses import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    product serializer
    """
    class Meta:
        """
        meta class
        """
        model = Product
        fields = "__all__"