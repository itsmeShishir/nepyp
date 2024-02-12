from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category_name','author', 'views_count', 'description','images','created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']