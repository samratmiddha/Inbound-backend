from rest_framework import viewsets
from mainapp.models import Question_Status
from mainapp.serializers import QuestionStatusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class QuestionStatusViewSet(viewsets.ModelViewSet):
    queryset=Question_Status.objects.all()
    serializer_class=QuestionStatusSerializer
    