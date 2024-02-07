from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated  
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializer import *

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)
    
    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)

    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return user_login(request)
    
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FreelancerRegistrationView(generics.CreateAPIView):
    serializer_class = FreelancerRegistrationSerializer

class SellerRegistrationView(generics.CreateAPIView):
    serializer_class = SellerRegistrationSerializer

class FreelancerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = FreelancerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Freelancer.objects.get(user=self.request.user)

class SellerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Seller.objects.get(user=self.request.user)
