from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializer import *

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

