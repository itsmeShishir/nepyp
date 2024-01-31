from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated  # Add this import
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

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return user_login(request)


#blog_category
class CategoryBlogListCreateView(generics.ListCreateAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [permissions.IsAdminUser | permissions.AllowAny]  
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            self.permission_denied(self.request)

        serializer.save()

class CategoryBlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [permissions.IsAdminUser] 

#blog
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

#Contact Us
class ContactUsCreateView(APIView):
    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
