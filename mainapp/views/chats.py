from rest_framework import viewsets
from mainapp.models import Chats
from mainapp.serializers import ChatsSerializer,ChatsDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import  status
from mainapp.permissions import FullAccessPermission,ReadOnly
 



class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['time']
    filterset_fields = ['time']
    ordering = ['time']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ChatsSerializer
        if self.action == 'retrieve':
            return ChatsSerializer
        return ChatsDefaultSerializer