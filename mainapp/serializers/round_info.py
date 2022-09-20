
from rest_framework import serializers
from mainapp.serializers.candidate import CandidateNameSerializer
from mainapp.serializers.interview_panel import InterviewPanelSerializer
from mainapp.serializers.round import RoundSerializer
from mainapp.models import Round_Info

class RoundInfoSerializer(serializers.ModelSerializer):
    student=CandidateNameSerializer()
    panel=InterviewPanelSerializer()
    round=RoundSerializer()
    class Meta:
        model=Round_Info
        fields='__all__'
