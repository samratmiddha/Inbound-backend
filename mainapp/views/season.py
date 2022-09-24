from rest_framework import viewsets
from mainapp.models import Season
from mainapp.serializers import SeasonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class SeasonViewSet(viewsets.ModelViewSet):
    queryset=Season.objects.all()
    serializer_class=SeasonSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['name','session','is_going','type']
    ordering=['session']

