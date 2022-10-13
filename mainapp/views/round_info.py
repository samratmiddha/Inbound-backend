from rest_framework import viewsets
from mainapp.models import Round_Info
from mainapp.serializers import RoundInfoSerializer
from mainapp.serializers import RoundInfoDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round_Info.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'season', 'type', 'start_date', 'end_date']
    filterset_fields = ['name', 'season', 'type', 'start_date', 'end_date']
    ordering = ['name']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RoundInfoSerializer
        if self.action == 'retrieve':
            return RoundInfoSerializer
        return RoundInfoDefaultSerializer
