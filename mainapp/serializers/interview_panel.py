
from rest_framework import serializers
from mainapp.models import Interview_Panel
class InterviewPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interview_Panel
        fields='__all__'
