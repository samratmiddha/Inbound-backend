from dataclasses import fields
from rest_framework import serializers
from mainapp.models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields='__all__'

class CandidateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields=['name','mobile_no']