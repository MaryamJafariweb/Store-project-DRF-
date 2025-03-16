from rest_framework import serializers
from product.models import ProductCategories, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image1')

