from django.contrib import admin
from .models import *


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message','created_at', 'updated_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at', 'updated_at']
