from rest_framework import viewsets
from mainapp.models import Question
from mainapp.serializers import QuestionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessPermission
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import QuestionDefaultSerializer
from rest_framework.decorators import action
from rest_framework import  status
from rest_framework.response import Response


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['question_text', 'section', 'asignee']
    filterset_fields = ['question_text', 'section', 'asignee']
    ordering = ['question_text']
    #permission_classes = [FullAccessPermission, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        if self.action == 'retrieve':
            return QuestionSerializer
        return QuestionDefaultSerializer
        
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

 

    