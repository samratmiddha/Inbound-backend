from rest_framework import viewsets
from mainapp.models import Question
from mainapp.serializers import QuestionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessPermission
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import QuestionDefualtSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['question_text', 'section', 'asignee']
    filterset_fields = ['question_text', 'section', 'asignee']
    ordering = ['question_text']
    permission_classes = [FullAccessPermission, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        if self.action == 'retrieve':
            return QuestionSerializer
        return QuestionDefualtSerializer
