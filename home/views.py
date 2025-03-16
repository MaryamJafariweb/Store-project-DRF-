from rest_framework import generics
from product.models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['offer', 'featured']


