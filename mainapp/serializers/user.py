
from rest_framework import serializers
from mainapp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['enrolment_number','name']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','enrolment_number','username','email','year']
