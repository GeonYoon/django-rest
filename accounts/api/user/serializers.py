import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.utils import timezone

from status.api.serializers import StatusInlineUserSerializer
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    status          = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status' # model name
        ]
    def get_uri(self,obj):
        return "/api/users/{id}/".format(id=obj.id)
    
    def get_status(self,obj):
        qs = obj.status_set.all().order_by("-timestamp")
        data = {
            'uri'   :self.get_uri(obj) + "status/",
            'last'  :StatusInlineUserSerializer(qs.first()).data,
            'recent_10':StatusInlineUserSerializer(qs[:10], many=True).data
        }
        return data
        
    # def get_status(self,obj):
    #     data = {
    #         'uri'       : self.get_uri(obj) + "status/",
    #         'recent'    : self.get_recent_status(obj)
    #     } 
    #     return data
        
    # def get_recent_status(self,obj):
    #     qs = obj.status_set.all().order_by("-timestamp")[:10] # Same thing as Status.objects.filter(user=obj)
    #     return StatusInlineUserSerializer(qs, many=True).data
