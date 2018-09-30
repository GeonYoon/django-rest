from django.conf.urls import url
from django.urls import path
from django.contrib import admin 
from .views import (
    StatusAPIView,
    # StatusCreateAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView
    )



urlpatterns = [
    path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
    path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]