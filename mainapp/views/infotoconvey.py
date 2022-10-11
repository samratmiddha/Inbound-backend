from rest_framework import viewsets
from mainapp.models import InfoToConvey
from mainapp.serializers import InfoToConveySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class InfoToConveyViewSet(viewsets.ModelViewSet):
    queryset=InfoToConvey.objects.all()
    serializer_class=InfoToConveySerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields=['student','is_conveyed','information']
    ordering_fields=['student','is_conveyed','information']
    ordering=['student']
    permission_classes=[IsAuthenticated]
    
    