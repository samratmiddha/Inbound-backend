from rest_framework import viewsets
from mainapp.models import Round
from mainapp.serializers import RoundSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class RoundViewSet(viewsets.ModelViewSet):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer
    