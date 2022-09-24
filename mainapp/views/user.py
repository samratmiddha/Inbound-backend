from django.shortcuts import get_object_or_404
from mainapp.serializers import UserSerializer,UserNameSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from mainapp.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer



    

