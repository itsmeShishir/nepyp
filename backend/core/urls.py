from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auths.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('contactus.urls')),
    path('api/', include('product.urls')),
]
