from django.conf.urls import url
from django.urls import path
from django.contrib import admin 
from .views import (
    StatusAPIView,
    StatusAPIDetailView,
    # StatusCreateAPIView,
    #StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
    )



urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusAPIDetailView.as_view(), name='detail'),
]