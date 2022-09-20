from rest_framework import viewsets
from mainapp.models import Question
from mainapp.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
