from django.urls import path
from .views import RegisterView, ProtecteView, CustomUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # ویو ثبت نام که خودمان ساختیم
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('protected_view/', ProtecteView.as_view()),
    path('profiles/', CustomUserView.as_view()),
    
    # ویوهای آماده simplejwt برای گرفتن و بازآوری توکن
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]