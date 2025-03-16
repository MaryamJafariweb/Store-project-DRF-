from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        ser = UserRegisterSerializer(data=request.POST)
        if ser.is_valid():
            ser.create(ser.validated_data)
            return Response(ser.data)
        return Response(ser.errors)
