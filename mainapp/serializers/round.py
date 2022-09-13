
from rest_framework import serializers
from mainapp.serializers.season import SeasonNameSerializer
from mainapp.models import Round

class RoundSerializer(serializers.ModelSerializer):
    season=SeasonNameSerializer()
    class Meta:
        model=Round
        fields='__all__'

class RoundNameSerializer(serializers.ModelSerializer):
    season=SeasonNameSerializer()
    class Meta:
        model=Round
        fields=['id','name','season']
