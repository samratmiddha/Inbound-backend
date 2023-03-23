
from rest_framework import serializers
from .season import SeasonNameSerializer
from .round import RoundSerializer
from ..models.candidate import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    season = SeasonNameSerializer()

    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'mobile_no', 'email','enrollment_number','is_exterminated','candidate_from','year']


class CandidateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name', 'id']


class CandidateDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class CSVFileSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
