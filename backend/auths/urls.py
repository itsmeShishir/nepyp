from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('a/', CustomLoginView.as_view(), name='custom_login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/freelancer/', FreelancerProfileView.as_view(), name='freelancer-profile'),
    path('profile/seller/', SellerProfileView.as_view(), name='seller-profile'),
    path('register/freelancer/', FreelancerRegistrationView.as_view(), name='freelancer-registration'),
    path('register/seller/', SellerRegistrationView.as_view(), name='seller-registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
