from rest_framework import viewsets
from mainapp.models import Question
from mainapp.models import Round_Info
from mainapp.models import Sectional_Marks
from mainapp.models import Section
from mainapp.serializers import RoundInfoSerializer
from mainapp.serializers import QuestionStatusDefaultSerializer
from mainapp.serializers import QuestionSerializer
from mainapp.serializers import SectionalMarksSerializer
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
    permission_classes = [FullAccessPermission, IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        if self.action == 'retrieve':
            return QuestionSerializer
        return QuestionDefaultSerializer
        

    def create(self, request, format=None):
        serializer = QuestionDefaultSerializer(data=request.data)
        print('ooo')
        if serializer.is_valid():
            instance =serializer.save()
            section_info_objects =Sectional_Marks.objects.filter(section=request.data['section'])
            section_info_serializer= SectionalMarksSerializer(section_info_objects,many=True)
            print(section_info_serializer.data)
            print('hhhh')
            print(instance.id)
            print('hhhh')
            for section_info in section_info_serializer.data:
                question_marks_serializer=QuestionStatusDefaultSerializer(data={
                'student':section_info['student']['id'],
                'question':instance.id,
                })
                print (section_info['student']['id'])
                if question_marks_serializer.is_valid():
                    question_marks_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

 

    