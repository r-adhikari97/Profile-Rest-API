from rest_framework import serializers
from profile_api import models


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing out APIView """
    name = serializers.CharField(max_length=10)


##------------------ Serializer ----------------------- ##

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a User profile Object"""

    class Meta:

        # Allows access to fields of model
        model = models.UserProfile
        fields = ('id','email','name','password')

        # making password Write only
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name= validated_data['name'],
            password=validated_data['password'],
        )

        return  user