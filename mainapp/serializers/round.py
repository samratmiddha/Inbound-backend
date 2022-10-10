
from rest_framework import serializers
from mainapp.models import Round

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model=Round
        fields='__all__'

class RoundNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Round
        fields=['id','name','season']
