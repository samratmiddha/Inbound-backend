
from rest_framework import serializers
from mainapp.serializers.section import SectionNameSerializer
from mainapp.serializers.user import UserNameSerializer
from mainapp.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    section = SectionNameSerializer()
    # asignee = UserNameSerializer()

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDefualtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
