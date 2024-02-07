from rest_framework import serializers
from .models import *


#category serializers
class CategoryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

#Blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

