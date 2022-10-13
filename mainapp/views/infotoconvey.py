from rest_framework import viewsets
from mainapp.models import InfoToConvey
from mainapp.serializers import InfoToConveySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import InfoToConveyCreateSerializer
from mainapp.serializers import InfoToConveySerializer


class InfoToConveyViewSet(viewsets.ModelViewSet):
    queryset = InfoToConvey.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student', 'is_conveyed', 'information']
    ordering_fields = ['student', 'is_conveyed', 'information']
    ordering = ['student']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return InfoToConveySerializer
        if self.action == 'retrieve':
            return InfoToConveySerializer
        return InfoToConveyCreateSerializer
