from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  viewsets
from rest_framework import status  # Handy HTTP Status codes
from profile_api import serializers  #
from profile_api import models

# autho
from rest_framework.authentication import TokenAuthentication
from profile_api import permissions
# Import Auth permissions to make it work
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Search Filter
from rest_framework import filters

class HelloAPIView(APIView):
    """ Test API View """
    # serializer_class
    serializer_class = serializers.HelloSerializer

    # //////////////////////////////////////////////////////////////////////////
    def get(self, request, format=None):

        """ Returns a list of APIView Features """

        an_apiview = [
            'uses HTTP method function (get, post, patch, put, delete)',
            'is similar to traditional DJANGO view',
            'Gives most control over app logic',
            'is mapped manually to urls',
        ]

        # Definining APi with get function
        return Response({'message': "Hello",
                         'an_apiview': an_apiview})

    # //////////////////////////////////////////////////////////////////////////

    def post(self, request):
        """ Create a hello message with our name """

        # self.serializer is a standard way to retrieve serializer value
        serializer = self.serializer_class(data=request.data)

        # Checking
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'

            return Response({'message': message})

        else:
            # Returns HTTP 400 bad request error

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # //////////////////////////////////////////////////////////////////////////

    def put(self,request,pk=None):
        """ Handles Updating an Object """
        return  Response ({'method':'PUT'})

    # //////////////////////////////////////////////////////////////////////////

    def patch(self,request,pk=None):
        """ Handles a partial update of an object """
        return  Response({'method':'PATCH'})

    # //////////////////////////////////////////////////////////////////////////

    def delete(self,request,pk=None):
        """ Responsible for Deleting values """
        return  Response ({'method':'DELETE'})




class HelloViewSets(viewsets.ViewSet):
    """ Test API View set """

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """ Returns a Hello Message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})


    def create(self,request):
        """ Create a New Hello Message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'HelloQ {name}'
            return  Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self,request,pk=None):
        """ Handle getting object bt ID """
        return  Response({'http_method':'GET'})


    def update(self,request,pk=None):
        """ Updates Values of object """
        return  Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        """ Handling \partially updating object """
        return  Response({'http_method':'PATCH'})


    def delete(self,request,pk=None):
        """ Handling deleting/Dstroying object """
        return  Response({'http_method':'DELETE'})





class UserProfileViewSet (viewsets.ModelViewSet):
     """ Handling , Creating and Updating profiles """
     serializer_class = serializers.UserProfileSerializer
     queryset = models.UserProfile.objects.all()
     authentication_classes = (TokenAuthentication,)
     permission_classes = (IsAuthenticatedOrReadOnly,permissions.UpdateOwProfile,)
     filter_backends = (filters.SearchFilter,)
     search_fields = ('name','email',)



