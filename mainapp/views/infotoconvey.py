from rest_framework import viewsets
from mainapp.models import InfoToConvey
from mainapp.serializers import InfoToConveySerializer

class InfoToConveyViewSet(viewsets.ModelViewSet):
    queryset=InfoToConvey.objects.all()
    serializer_class=InfoToConveySerializer
    