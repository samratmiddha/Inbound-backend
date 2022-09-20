from rest_framework import viewsets
from mainapp.models import Round
from mainapp.serializers import RoundSerializer

class RoundViewSet(viewsets.ModelViewSet):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer
    