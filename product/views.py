from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySrz, CategoryNameSrz, CommentSerializer
from .models import Product, ProductBrand, ProductCategories, Comment


# Create your views here.

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        ser = ProductListSerializer(instance=products, many=True)
        return Response(ser.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        detail = Product.objects.get(id=pk)
        if detail.is_active == True:
            srz = ProductDetailSerializer(instance=detail)
            return Response(srz.data)

    def post(self, request, pk):
        comments = Comment.objects.get(id=pk)
        srz = CommentSerializer(data=request.data,  context={'request': request}, instance=comments)
        if srz.is_valid():
            srz.save()
            return Response({'request': 'done'})
        return Response(srz.errors)



