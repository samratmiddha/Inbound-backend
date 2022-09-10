
from rest_framework import serializers
from mainapp.models import Round_Info
class RoundInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Round_Info
        fields='__all__'
