from rest_framework import viewsets
from mainapp.models import InfoToConvey
from mainapp.serializers import InfoToConveySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import InfoToConveyCreateSerializer
from mainapp.serializers import InfoToConveySerializer
from rest_framework.decorators import action
from rest_framework import  status
from rest_framework.response import Response


class InfoToConveyViewSet(viewsets.ModelViewSet):
    queryset = InfoToConvey.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student', 'is_conveyed', 'information','season']
    ordering_fields = ['student', 'is_conveyed', 'information']
    ordering = ['is_conveyed']
    permission_classes = [IsAuthenticated]
    allowed_method = ['get', 'post', 'head', 'patch', 'put']

    def get_serializer_class(self):
        if self.action == 'list':
            return InfoToConveySerializer
        if self.action == 'retrieve':
            return InfoToConveySerializer
        return InfoToConveyCreateSerializer

    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)