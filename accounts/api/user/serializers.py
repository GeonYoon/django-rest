import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
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
        # return "/api/users/{id}/".format(id=obj.id)
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={"username": obj.username},request=request)
    
    def get_status(self,obj):
        # https://django-geonyoon.c9users.io/api/user/gun/?limit=5 ---> use like this
        request = self.context.get('request')
        limit   = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        
        qs = obj.status_set.all().order_by("-timestamp")
        data = {
            'uri'   :self.get_uri(obj) + "status/",
            'last'  :StatusInlineUserSerializer(qs.first(), context={'request': request}).data,
            'recent':StatusInlineUserSerializer(qs[:limit], context={'request': request}, many=True).data
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
