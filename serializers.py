from rest_framework import serializers
from .models import ProductModel

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"