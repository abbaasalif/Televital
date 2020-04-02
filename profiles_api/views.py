from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
class HelloApiView(APIView):
    """Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):
        """Returns a list of API features"""
        an_apiview = ['Uses HTTP methods as functions (get,post,patch,put,delete)',
    'Is similar to a traditional Django View',
    'Gives you the most control over Application logic',
    'Is mapped manually to URLs',
    ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        a_viewset=['Uses actions (list,create,retrive,update,partial_update)',
        'Automatically maps to URLs using routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """Handle getting a object by id"""
        return Response({'http_method':'GET'})
    def update(self, request, pk =None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        """Handle patial updating"""
        return Response({'http_method':'PATCH'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends= (DjangoFilterBackend,)
    filterset_fields = ('is_doctor',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
class PatientVitalsViewset(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes = (
    permissions.UpdateOwnVitals,
    IsAuthenticated
    )
    serializer_class=serializers.ProfileVitalsSerializer
    queryset = models.ProfileVitals.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
