from rest_framework import viewsets
from mainapp.models import Round
from mainapp.serializers import RoundSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class RoundViewSet(viewsets.ModelViewSet):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['name','season','type','start_date','end_date']
    filterset_fields=['name','season','type','start_date','end_date']
    ordering=['name']
    permission_classes=[IsAuthenticated]

    