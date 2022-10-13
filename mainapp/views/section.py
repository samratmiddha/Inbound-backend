from rest_framework import viewsets
from mainapp.models import Section
from mainapp.serializers import SectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import SectionDefaultSerializer


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
