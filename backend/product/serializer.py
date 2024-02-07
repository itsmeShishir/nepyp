from rest_framework import serializers
from auths.serializer import UserSerializer
from .models import *

#CAtegory and SubCategory and product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'images', 'created_at', 'updated_at']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'description', 'images', 'created_at', 'updated_at']

class ProductsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    subcategory = SubCategorySerializer()

    class Meta:
        model = Products
        fields = '__all__'

class SclorshipSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = Sclorship
        fields = '__all__'

class BrotherSisterCompanySerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = BrotherSisterCompany
        fields = '__all__'