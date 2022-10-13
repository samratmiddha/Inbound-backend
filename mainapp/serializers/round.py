
from rest_framework import serializers
from mainapp.models import Round
from mainapp.serializers.season import SeasonNameSerializer


class RoundSerializer(serializers.ModelSerializer):
    season = SeasonNameSerializer()

    class Meta:
        model = Round
        fields = '__all__'


class RoundNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'name', 'season']


class RoundDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'
