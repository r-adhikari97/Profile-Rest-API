from rest_framework.views import APIView
from rest_framework.response import  Response


class HelloAPIView(APIView):
    """ Test API View """
    def get(self, request, format=None):

        """ Returns a list of APIView Features """

        an_apiview =[
            'uses HTTP method function (get, post, patch, put, delete)',
            'is similar to traditional DJANGO view',
            'Gives most control over app logic',
            'is mapped manually to urls',
        ]

        # Definining APi with get function
        return  Response({'message': "Hello",
                          'an_apiview': an_apiview })