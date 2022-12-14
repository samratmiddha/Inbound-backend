
from rest_framework import serializers
from mainapp.serializers.section import SectionNameSerializer
from mainapp.serializers.user import UserNameSerializer
from ..models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    section = SectionNameSerializer()
    asignee = UserNameSerializer(many=True)  

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
