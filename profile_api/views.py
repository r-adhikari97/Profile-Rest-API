from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status  # Handy HTTP Status codes
from profile_api import serializers  #


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