
from rest_framework import serializers
from mainapp.serializers.season import SeasonNameSerializer
from mainapp.serializers.round import RoundSerializer
from mainapp.models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    rounds=RoundSerializer(many=True)
    season=SeasonNameSerializer()
    class Meta:
        model=Candidate
        fields='__all__'

class CandidateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields=['id','name','mobile_no','email']

class CandidateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields=['name','id']