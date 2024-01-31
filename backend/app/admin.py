from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'phone', 'role', 'is_active', 'is_staff', 'get_date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'role', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'username']
    ordering = ['email']

    def get_date_joined(self, obj):
        return obj.date_joined

    get_date_joined.short_description = 'Date Joined'

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'pan','linkedin', 'location', 'contact_number')
    search_fields = ('user__email', 'name')
    ordering = ('user__email',)

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'location', 'pan', 'services', 'website', 'designation')
    search_fields = ('user__email', 'name')
    ordering = ('user__email',)

@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message','created_at', 'updated_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at', 'updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'images', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'images', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
