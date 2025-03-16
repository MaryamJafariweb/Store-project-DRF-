from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from .cart import Cart
from .serializers import CartSerializers, OrderItemSerializer, OrderSerializer
from product.models import Product
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class OrderingView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        cart = Cart(request)
        srz = CartSerializers(instance=cart, many=True)
        return Response(srz.data)


class AddCartView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        srz = OrderItemSerializer(instance=product)
        return Response(srz.data)

    def post(self, request, product_id):
        cart = Cart(request)
        product = OrderItem.objects.get(Product, product_id)
        srz = OrderItemSerializer(data=request.data)
        if srz.is_valid():
            cart.add(product, srz.data)
            return Response({'response': 'Done'})
        return Response(srz.errors)


class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        srz = OrderSerializer(instance=order)
        return Response(srz.data)

