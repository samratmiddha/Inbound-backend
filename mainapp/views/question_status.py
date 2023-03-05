from rest_framework import viewsets
from mainapp.models import Question_Status
from mainapp.models import Sectional_Marks
from mainapp.models import Round_Info
from mainapp.models import Question
from mainapp.models import Section
from mainapp.serializers import QuestionStatusSerializer
from mainapp.serializers import QuestionDefaultSerializer
from mainapp.serializers.sectional_marks import SectionalMarksDefaultSerializer
from mainapp.serializers import SectionDefaultSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.permissions import FullAccessQuestionMarksPermission
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import QuestionStatusDefaultSerializer
from rest_framework.decorators import action
from rest_framework import  status
from rest_framework.response import Response
from django.http import JsonResponse
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class QuestionStatusViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Question_Status.objects.all()
    ordering_fields = ['question', 'student',
                       'marks', 'normalized_marks', 'is_checked']
    filterset_fields = ['question', 'student',
                        'marks', 'normalized_marks', 'is_checked']
    ordering = ['marks']
    permission_classes = [FullAccessQuestionMarksPermission, IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionStatusSerializer
        if self.action == 'retrieve':
            return QuestionStatusSerializer
        return QuestionStatusDefaultSerializer

    def update(self,request,pk,*args,**kwargs):
        object = Question_Status.objects.get(pk=pk)
        serializer=QuestionStatusDefaultSerializer(object,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("wrong parameters")
        question_object=Question.objects.get(pk=serializer.data['question'])
        question_serializer=QuestionDefaultSerializer(question_object)

        sectional_marks_objects=Sectional_Marks.objects.filter(student=serializer.data['student'],section=question_serializer.data['section'])
        all_sectional_marks_objects=Sectional_Marks.objects.filter(section=question_serializer.data['section'])
        section_object=Section.objects.get(pk=question_serializer.data['section'])
        section_serializer=SectionDefaultSerializer(section_object)
        round_info_objects=Round_Info.objects.filter(student=serializer.data['student'],round=section_serializer.data['round'])
        all_round_info_objects=Round_Info.objects.filter(round=section_serializer.data['round'])
        for object in sectional_marks_objects:
            object.sectional_marks
        for object in all_sectional_marks_objects:
            object.normalize
        for round_info_object in round_info_objects:
            round_info_object.marks_obtained
        for round_info_object in all_round_info_objects:
            round_info_object.normalize
        
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        'IMG',
        {
        'type':'echo_message',
        'message': 'Test message'
        }
)
        return Response(serializer.data)

        
        
    def get(self,request):
        objects = Question_Status.objects.all()
        Serializer = get_serializer_class(self)
        valid_pks= []  
        for object in objects:
            if FullAccessQuestionMarksPermission.has_object_permission(self,request, object):
                valid_pks.append(object.pk)
        filtered_objects=Question_Status.objects.filter(pk__in=valid_pks)
        serializer=Serializer(filtered_objects)
        return Response(serializer.data)

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

    @action(methods=['GET'],detail=False,url_path='get_status_by_question/(?P<question_id>\d+)',url_name='get_status_by_question')
    def get_status_by_question(self,request,question_id):
        queryset = Question_Status.objects.filter(question=question_id)
        seraializer = QuestionStatusSerializer(queryset,many=True)
        unchecked=[]
        checked=[]
        for question_status in seraializer.data:
            if question_status['marks'] == None:
                unchecked.append(question_status)
            else:
                checked.append(question_status)
        return Response({"checked":checked , "unchecked":unchecked})




    
        


    