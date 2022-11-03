
from rest_framework import serializers
from mainapp.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['name','enrolment_number','username']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['name','enrolment_number','username','email','year']
