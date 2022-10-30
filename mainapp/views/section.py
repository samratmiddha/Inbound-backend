from rest_framework import viewsets
from mainapp.models import Section
from mainapp.serializers import SectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import SectionDefaultSerializer
from rest_framework.decorators import action
from rest_framework import  status



class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['round', 'max_marks', 'name', 'weightage']
    filterset_fields = ['round', 'max_marks', 'name', 'weightage']
    ordering = ['round']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return SectionSerializer
        if self.action == 'retrieve':
            return SectionSerializer
        return SectionDefaultSerializer
 
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)