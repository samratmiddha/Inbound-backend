
from rest_framework import serializers
from ..models.season import Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class SeasonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'name']
