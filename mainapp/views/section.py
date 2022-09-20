from rest_framework import viewsets
from mainapp.models import Section
from mainapp.serializers import SectionSerializer

class SectionViewSet(viewsets.ModelViewSet):

    queryset=Section.objects.all()
    serializer_class=SectionSerializer

    