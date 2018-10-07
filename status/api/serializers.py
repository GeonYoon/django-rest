from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse
'''
Serializers --> JSON
Serializers --> vlaidate data 
'''

'''
Serializers allow complex data such as querysets and model instances to be 
converted to native Python datatypes that can be easily rendered into JSON, XML, or other content type

We can create and update things with serializers but deleting things

Each field in a Form class is responsible not only for validating data, 
but also for "cleaning" it — normalizing it to a consistent format
'''
# class CustomSerializer(serializers.Serializers):
#     content =        serializers.CharField()
#     email   =        serializers.EmailField()
    


class StatusSerializer(serializers.ModelSerializer):
    uri     = serializers.SerializerMethodField(read_only=True)
    # user    = serializers.SerializerMethodField(read_only=True)
    user    = UserPublicSerializer(read_only = True)
    class Meta:
        model = Status
        fields = [
            'id', #?
            'user',
            'content',
            'image',
            'uri',
        ]
        read_only_fields = ['user'] # GET # readonly_fields
    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={"request" : request}).data
        
    def get_uri(self, obj):
        request = self.context.get('request')
        # return "/api/status/{id}/".format(id=obj.id)
        return api_reverse('api-status:detail', kwargs={'id' : obj.id}, request=request)
    
    # def validate_<fieldname>(self, value) i.e. validate_content
    
    # def validate_content(self, value):
    #     if len(value) > 1000:
    #         raise serializers.ValidationError("this is way too long.")
    #     return value
        
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")
        return data

# inherit StatusSerializer        
class StatusInlineUserSerializer(StatusSerializer):
    # uri     = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id', #?
            'content',
            'image',
            'uri',
        ]
        
    # def get_uri(self, obj):
    #     return "/api/status/{id}/".format(id=obj.id)            
            
            
            