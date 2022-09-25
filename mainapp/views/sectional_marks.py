from rest_framework import viewsets
from mainapp.models import Sectional_Marks
from mainapp.serializers import SectionalMarksSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessPermission
from rest_framework.permissions import IsAuthenticated



class SectionalMarksViewSet(viewsets.ModelViewSet):

    queryset=Sectional_Marks.objects.all()
    serializer_class=SectionalMarksSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['student','section','marks']
    ordering=['student']
    permission_classes=[FullAccessPermission,IsAuthenticated]