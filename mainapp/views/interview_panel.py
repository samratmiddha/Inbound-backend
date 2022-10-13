from rest_framework import viewsets
from mainapp.models import Interview_Panel
from mainapp.serializers import InterviewPanelSerializer
from mainapp.serializers import InterviewPanelDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class InterviewPanelViewSet(viewsets.ModelViewSet):
    queryset = Interview_Panel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['members', 'season', 'is_active', 'location', 'type']
    filterset_fields = ['members', 'season', 'is_active', 'location', 'type']
    ordering = ['is_active']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return InterviewPanelSerializer
        if self.action == 'retrieve':
            return InterviewPanelSerializer
        return InterviewPanelDefaultSerializer
