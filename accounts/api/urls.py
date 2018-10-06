from django.contrib import admin
from django.urls import include, path

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # accounts app 
from .views import AuthAPIView, RegisterAPIView

urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]