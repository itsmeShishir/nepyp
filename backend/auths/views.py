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
    

class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Attempting login for email: {email}")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            print(f"Login failed for email: {email}, password: {password}")

            # Check if the user with the provided email exists
            existing_user = CustomUser.objects.filter(email=email).first()

            if existing_user is None:
                # User with the provided email does not exist
                return Response({'detail': 'Email does not match'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                # User with the provided email exists, but the password does not match
                return Response({'detail': 'Password does not match'}, status=status.HTTP_401_UNAUTHORIZED)


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

