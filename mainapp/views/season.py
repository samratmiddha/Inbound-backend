from rest_framework import viewsets
from mainapp.models import Season
from mainapp.serializers import SeasonSerializer


class SeasonViewSet(viewsets.ModelViewSet):
    queryset=Season.objects.all()
    serializer_class=SeasonSerializer