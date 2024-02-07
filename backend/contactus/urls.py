from django.urls import path
from .views import *

urlpatterns = [
    #Contact Us
    path('contactus/', ContactUsCreateView.as_view(), name='contactus-create'),
]
