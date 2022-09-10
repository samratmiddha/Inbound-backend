
from rest_framework import serializers
from mainapp.models import Question_Status
class QuestionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question_Status
        fields='__all__'
