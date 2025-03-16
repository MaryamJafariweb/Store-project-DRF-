from rest_framework import serializers
from .models import Product, ProductCategories, Comment


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image1', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('name', 'category', 'image1', 'image2', 'image3',
                  'price', 'short_description', 'description', 'is_active',
                  'offer', 'featured', 'brand')


class CategoryNameSrz(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ('name',)


class CategorySrz(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ('name', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
