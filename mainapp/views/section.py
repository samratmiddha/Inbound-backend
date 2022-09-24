from rest_framework import viewsets
from mainapp.models import Section
from mainapp.serializers import SectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class SectionViewSet(viewsets.ModelViewSet):

    queryset=Section.objects.all()
    serializer_class=SectionSerializer

    