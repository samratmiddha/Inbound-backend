from rest_framework import viewsets
from mainapp.models import Question_Status
from mainapp.serializers import QuestionStatusSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessPermission
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import QuestionStatusDefaultSerializer
from rest_framework.decorators import action
from rest_framework import  status
from rest_framework.response import Response
import json

class QuestionStatusViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Question_Status.objects.all()
    ordering_fields = ['question', 'student',
                       'marks', 'normalized_marks', 'is_checked']
    filterset_fields = ['question', 'student',
                        'marks', 'normalized_marks', 'is_checked']
    ordering = ['question']
    # permission_classes = [FullAccessPermission, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionStatusSerializer
        if self.action == 'retrieve':
            return QuestionStatusSerializer
        return QuestionStatusDefaultSerializer
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    @action(methods=['POST'],detail=False,url_name='multiple_retrieve/')
    def multiple_retrieve(self,request,*args,**kwargs):
        data=self.request.data
        print(self.request.data)
        studentId=data['studentId']
        response=[]
        for question in data['questions']:
            questionId =question['id']
            obj=Question_Status.objects.all().filter(student=studentId,question=questionId  )
            serializer = QuestionStatusSerializer(obj,many=True)
            response.append(serializer.data)
        return Response(response)
        return Response('hii')