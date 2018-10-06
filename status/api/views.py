import json
from rest_framework import generics, mixins, permissions 
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response 
#from django.views.generic import view
from django.shortcuts import get_object_or_404

from accounts.api.permissions import IsOwnerOrReadOnly
from status.models import Status
from .serializers import StatusSerializer


# # CreateModelMixin --- POST method
# # UpdateModelMixin --- PUT method
# # DestoryModelMixin --- Delete method

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                ='id'
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
 
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None
    
    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)

#Login required mixin / decorator 

class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView): 
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly] # is this person authenticated or not?
    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    passed_id                   = None
    
    def get_queryset(self):
        request = self.request # prevent us to type self.request every single time 
        # print(request.user)
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs 
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # This method allows us to create instance without inputting user id (insde of content)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# class StatusListSearchAPIView(APIView):
#     permission_classes          = []
#     authentication_classes      = []
    
#     def get(self,request,format=None):
#         qs = Status.objects.all()
#         # If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
        
#     def post(self,request,format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
        
# '''
# The mixin classes provide the actions that are used to provide the basic view behavior.
# Note that the mixin classes provide action methods rather than defining the handler methods,
# such as .get() and .post(), directly.
# '''

# # CreateModelMixin --- POST method
# # UpdateModelMixin --- PUT method
# # DestoryModelMixin --- Delete method

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): # Create List
#     permission_classes          = []
#     authentication_classes      = []
#     # queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
    
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__iscontains=query)
#         return qs 
    
#     # [self.create()] comes from mixin.CreateModelMixin
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
  
# # class StatusCreateAPIView(generics.CreateAPIView):   ---> This class is replaced by mixin.CreateModelMixin
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
    
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# # This can literally replace entire mixin things below!! 
# # class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer

# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.RetrieveAPIView):
#     permission_classes          = []
#     authentication_classes      = []
#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
#     # allow us to do [<int:id>/]
#     lookup_field                = 'id' # you can use 'slug'
    
#     # you can  do like this instead of using lookup_field
#     # def get_object(self, *args, **kwargs):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
        
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
        
    
# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     lookup_field                = 'id' # you can use 'slug'

# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     lookup_field                = 'id' # you can use 'slug'