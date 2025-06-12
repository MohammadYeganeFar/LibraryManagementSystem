from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # به هر کسی اجازه دسترسی به این ویو را می‌دهیم
    serializer_class = RegisterSerializer

class ProtecteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        username = request.user.username
        return Response({'message':f'hello {username}'})