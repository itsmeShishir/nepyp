from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  

urlpatterns = [
   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    #Blog_category
    path('category_blogs/', CategoryBlogListCreateView.as_view(), name='category-blog-list-create'),
    path('category_blogs/<int:pk>/', CategoryBlogRetrieveUpdateDestroyView.as_view(), name='category-blog-retrieve-update-destroy'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
]
