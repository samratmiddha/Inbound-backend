
from rest_framework import serializers
from mainapp.serializers.user import UserNameSerializer
from mainapp.serializers.candidate import CandidateNameSerializer
from mainapp.serializers.round import RoundNameSerializer
from ..models.interview_panel import Interview_Panel



class InterviewPanelSerializer(serializers.ModelSerializer):
    members = UserNameSerializer(many=True)
    current_student=CandidateNameSerializer()
    current_round=RoundNameSerializer()
    class Meta:
        model = Interview_Panel
        fields = '__all__'


class InterviewPanelLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview_Panel
        fields = ['id', 'location']


class InterviewPanelDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview_Panel
        fields = '__all__'
