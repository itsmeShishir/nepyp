from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'phone', 'role', 'is_active', 'is_staff', 'password']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'role', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'username']
    ordering = ['email']


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

