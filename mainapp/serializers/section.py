
from rest_framework import serializers
from mainapp.serializers.round import RoundNameSerializer
from mainapp.models import Section

class SectionSerializer(serializers.ModelSerializer):
    round=RoundNameSerializer()
    class Meta:
        model=Section
        fields='__all__'

class SectionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields=['id','round','name']