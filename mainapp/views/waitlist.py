from mainapp.models import Waitlist
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from mainapp.serializers import WaitlistDefaultSerializer
from mainapp.serializers import WaitlistSerializer



class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['student', 'round', 'season','time']
    filterset_fields = ['student', 'round', 'season']
    ordering = ['time']
    permission_classes = [IsAuthenticated]

    

    def get_serializer_class(self):
        if self.action == 'list':
            return WaitlistSerializer
        if self.action == 'retrieve':
            return WaitlistSerializer
        return WaitlistDefaultSerializer