from rest_framework import viewsets
from mainapp.models import Interview_Panel
from mainapp.serializers import InterviewPanelSerializer

class InterviewPanelViewSet(viewsets.ModelViewSet):
    queryset=Interview_Panel.objects.all()
    serializer_class=InterviewPanelSerializer