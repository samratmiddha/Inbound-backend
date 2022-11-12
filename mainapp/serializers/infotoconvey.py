from rest_framework import serializers
from ..models.infotoconvey import InfoToConvey
from mainapp.serializers.candidate import CandidateContactSerializer

class InfoToConveySerializer(serializers.ModelSerializer):

    student = CandidateContactSerializer()
    class Meta:
        model=InfoToConvey
        fields='__all__'

class InfoToConveyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=InfoToConvey
        fields='__all__'