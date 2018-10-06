from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
#from .utils import jwt_response_payload_handler

from accounts.api.permissions import AnonPermissionOnly
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from .serializers import UserDetailSerializer


User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes  = [permissions.IsAuthenticatedOrReadOnly] 
    serializer_class    = UserDetailSerializer
    queryset            = User.objects.filter(is_active=True)
    lookup_field        = 'username' #id
    
class UserStatusAPIView(generics.ListAPIView):
    serializer_class    = StatusInlineUserSerializer
    
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username",None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)

    
    