from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView  
from .views import RegisterView, LoginView, favicon_view

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
