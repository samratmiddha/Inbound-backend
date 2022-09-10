
from rest_framework import serializers
from mainapp.models import User
class UserlSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
