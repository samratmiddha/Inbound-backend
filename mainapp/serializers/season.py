
from rest_framework import serializers
from mainapp.models import Season
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Season
        fields='__all__'
