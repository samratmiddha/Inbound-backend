from mainapp.models.waitlist import Waitlist
from rest_framework import serializers
from mainapp.serializers import CandidateDefaultSerializer
from mainapp.serializers import RoundDefaultSerializer





class WaitlistDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = '__all__'

class WaitlistSerializer(serializers.ModelSerializer):
    student = CandidateDefaultSerializer()
    round =  RoundDefaultSerializer()
    class Meta: 
        model=Waitlist
        fields= ['student','round','season']