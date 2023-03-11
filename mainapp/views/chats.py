from rest_framework import viewsets
from mainapp.models import Chats
from mainapp.serializers import ChatsSerializer,ChatsDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import  status
from mainapp.permissions import FullAccessPermission,ReadOnly
from rest_framework.response import Response
 



class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['time']
    filterset_fields = ['time','panel']
    ordering = ['-time']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ChatsSerializer
        if self.action == 'retrieve':
            return ChatsSerializer
        return ChatsDefaultSerializer
    
    def list(self, request):
        panel = self.request.query_params.get('panel')
        if panel=="null":
            queryset = Chats.objects.filter(panel__isnull=True).order_by("-time")
        else:
            queryset=Chats.objects.filter(panel=panel).order_by("-time")
        serializer = ChatsSerializer(queryset, many=True)
        return Response(serializer.data)