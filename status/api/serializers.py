from rest_framework import serializers
from status.models import Status

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
    class Meta:
        model = Status
        fields = [
            'id', #?
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user'] # GET # readonly_fields
        
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
            
            
            
            
            