from rest_framework import viewsets
from mainapp.models import Section
from mainapp.serializers import SectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class SectionViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['round','max_marks','name','weightage']
    filterset_fields=['round','max_marks','name','weightage']
    ordering=['round']
    permission_classes=[IsAuthenticated]




    