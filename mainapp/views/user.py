from django.shortcuts import get_object_or_404
from mainapp.serializers import UserSerializer,UserNameSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from mainapp.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer



    

