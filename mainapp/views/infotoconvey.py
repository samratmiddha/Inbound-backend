from rest_framework import viewsets
from mainapp.models import InfoToConvey
from mainapp.serializers import InfoToConveySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class InfoToConveyViewSet(viewsets.ModelViewSet):
    queryset=InfoToConvey.objects.all()
    serializer_class=InfoToConveySerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['student','isconveyed','information']
    ordering=['student']
    
    