
from rest_framework import serializers
from mainapp.serializers.candidate import CandidateContactSerializer
from mainapp.serializers.interview_panel import InterviewPanelSerializer
from mainapp.serializers.round import RoundSerializer
from ..models.round_info import Round_Info


class RoundInfoSerializer(serializers.ModelSerializer):
    student = CandidateContactSerializer()
    panel = InterviewPanelSerializer()
    round = RoundSerializer()
    time_start= serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Round_Info
        fields = '__all__'


class RoundInfoDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round_Info
        fields = '__all__'

class RoundInfoJuniorSerializer(serializers.ModelSerializer):
    student = CandidateContactSerializer()
    panel = InterviewPanelSerializer()
    round = RoundSerializer()
    class Meta:
        model = Round_Info
        exclude=['_marks_obtained']