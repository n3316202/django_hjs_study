from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

#http://127.0.0.1:8000/user/token/
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
