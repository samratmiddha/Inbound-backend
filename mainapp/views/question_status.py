from rest_framework import viewsets
from mainapp.models import Question_Status
from mainapp.serializers import QuestionStatusSerializer

class QuestionStatusViewSet(viewsets.ModelViewSet):
    queryset=Question_Status.objects.all()
    serializer_class=QuestionStatusSerializer
    