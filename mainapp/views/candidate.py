from rest_framework import viewsets
from mainapp.models import Candidate
from mainapp.serializers import CandidateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class CandidiateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['name','email','branch','enrolment_number']
    ordering=['name']
    permission_classes=[IsAuthenticated]