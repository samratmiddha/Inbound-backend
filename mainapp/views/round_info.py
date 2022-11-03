from rest_framework import viewsets
from mainapp.models import Round_Info
from mainapp.serializers import RoundInfoSerializer
from mainapp.serializers import RoundInfoDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class RoundInfoViewSet(viewsets.ModelViewSet):
    queryset = Round_Info.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['student', 'round', 'panel','marks_obtained']
    filterset_fields = ['student', 'round', 'panel']
    ordering = ['marks_obtained']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RoundInfoSerializer
        if self.action == 'retrieve':
            return RoundInfoSerializer
        return RoundInfoDefaultSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(RoundInfoDefaultSerializer(instance.parent).data)
 

    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)