from rest_framework import viewsets
from mainapp.models import Sectional_Marks
from mainapp.serializers import SectionalMarksSerializer
from mainapp.serializers import SectionalMarksDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import  status



class SectionalMarksViewSet(viewsets.ModelViewSet):

    queryset = Sectional_Marks.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['student', 'section', 'marks']
    filterset_fields = ['student', 'section', 'marks']
    ordering = ['student']
    # permission_classes = [FullAccessPermission, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return SectionalMarksSerializer
        if self.action == 'retrieve':
            return SectionalMarksSerializer
        return SectionalMarksDefaultSerializer

    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)