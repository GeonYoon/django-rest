from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response 
#from django.views.generic import view

from status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []
    
    def get(self,request,format=None):
        qs = Status.objects.all()
        # If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
        
    def post(self,request,format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)
        
'''
The mixin classes provide the actions that are used to provide the basic view behavior.
Note that the mixin classes provide action methods rather than defining the handler methods,
such as .get() and .post(), directly.
'''

# CreateModelMixin --- post data
# UpdateModelMixin --- put data
class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): # Create List
    permission_classes          = []
    authentication_classes      = []
    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__iscontains=query)
        return qs 
    
    # [self.create()] comes from mixin.CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
  
# class StatusCreateAPIView(generics.CreateAPIView):   ---> This class is replaced by mixin.CreateModelMixin
#     permission_classes          = []
#     authentication_classes      = []
#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    # allow us to do [<int:id>/]
    lookup_field                = 'id' # you can use 'slug'
    
    # you can  do like this instead of using lookup_field
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)
    
class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' # you can use 'slug'

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' # you can use 'slug'