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

#Category
class ProductsCategoryView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#SubCategory
class ProductsSubCategoryView(APIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

#product
class ProductsView(APIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

#Sclorship
class SclorshipView(APIView):
    queryset = Sclorship.objects.all()
    serializer_class = SclorshipSerializer

#BrotherSisterCompany
class BrothersisterView(APIView):
    queryset = BrotherSisterCompany.objects.all()
    serializer_class = BrotherSisterCompanySerializer
    