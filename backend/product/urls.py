from django.urls import path
from .views import *

urlpatterns = [
    #products
    path('category/', ProductsCategoryView.as_view(), name='product-category'),
    path('category/subcategory', ProductsSubCategoryView.as_view(), name='product-subcatgory'),
    path('product/', ProductsView.as_view(), name='product-lists'),
    path('product/sclorship/', SclorshipView.as_view(), name='product-sclorship'),
    path('product/brothersister/', BrothersisterView.as_view(), name='brothersister-lists'),
]
