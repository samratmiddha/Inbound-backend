from rest_framework import viewsets
from mainapp.models import Candidate
from mainapp.serializers import CandidateSerializer

class CandidiateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer