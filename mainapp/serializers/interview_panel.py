
from rest_framework import serializers
from mainapp.serializers.user import UserNameSerializer
from mainapp.models import Interview_Panel

class InterviewPanelSerializer(serializers.ModelSerializer):
    members = UserNameSerializer(many=True)
    class Meta:
        model=Interview_Panel
        fields='__all__'

class InterviewPanelLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interview_Panel
        fields=['id','location']
