from rest_framework import viewsets
from mainapp.models import Round
from mainapp.serializers import RoundSerializer
from mainapp.serializers import RoundDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import  status



class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'season', 'type', 'start_date', 'end_date']
    filterset_fields = ['name', 'season', 'type', 'start_date', 'end_date']
    ordering = ['name']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RoundSerializer
        if self.action == 'retrieve':
            return RoundSerializer
        return RoundDefaultSerializer
        
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)