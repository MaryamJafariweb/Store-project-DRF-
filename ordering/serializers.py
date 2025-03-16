from rest_framework import serializers
from product.models import Product
from .models import OrderItem, Order


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
