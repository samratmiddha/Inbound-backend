from django.shortcuts import get_object_or_404
from mainapp.serializers import UserSerializer,UserNameSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from mainapp.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['username','name','email','enrolment_number']
    ordering=['name']
    permission_classes=[IsAuthenticated]
    



    

