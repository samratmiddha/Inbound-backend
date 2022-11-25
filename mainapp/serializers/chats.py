
from rest_framework import serializers
from ..models.chats import Chats
from mainapp.serializers import UserInfoSerializer

class ChatsSerializer(serializers.ModelSerializer):
    sender=UserInfoSerializer()
    class Meta:
        model = Chats
        fields = '__all__'

class ChatsDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = '__all__'