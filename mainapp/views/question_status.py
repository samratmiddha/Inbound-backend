from rest_framework import viewsets
from mainapp.models import Question_Status
from mainapp.serializers import QuestionStatusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class QuestionStatusViewSet(viewsets.ModelViewSet):
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    queryset=Question_Status.objects.all()
    serializer_class=QuestionStatusSerializer
    ordering_fields=['question','student','marks','normalized_marks','is_checked']
    ordering=['question']
    