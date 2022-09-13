
from rest_framework import serializers
from mainapp.serializers.candidate import CandidateNameSerializer
from mainapp.serializers.question import QuestionSerializer
from mainapp.models import Question_Status

class QuestionStatusSerializer(serializers.ModelSerializer):
    question=QuestionSerializer()
    student=CandidateNameSerializer()
    class Meta:
        model=Question_Status
        fields='__all__'
