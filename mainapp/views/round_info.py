from rest_framework import viewsets
from mainapp.models import Round_Info
from mainapp.models import Section
from mainapp.models import Sectional_Marks
from mainapp.models import Question_Status
from mainapp.models import Question
from mainapp.serializers.round_info import RoundInfoSerializer
from mainapp.serializers.round_info import RoundInfoDefaultSerializer
from mainapp.serializers.sectional_marks import SectionalMarksSerializer
from mainapp.serializers import QuestionStatusSerializer
from mainapp.serializers.sectional_marks import SectionalMarksDefaultSerializer
from mainapp.serializers import QuestionStatusDefaultSerializer
from mainapp.serializers import SectionDefaultSerializer
from mainapp.serializers import QuestionDefaultSerializer
from mainapp.serializers.round_info import RoundInfoJuniorSerializer
from mainapp.permissions import FullAccessRoundMarksPermission

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
import rest_framework.permissions as drf_permissions
import math
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



class RoundInfoViewSet(viewsets.ModelViewSet):
    queryset = Round_Info.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['student', 'round', 'panel','marks_obtained']
    filterset_fields = ['student', 'round', 'panel']
    ordering = ['-_marks_obtained']
    permission_classes = [IsAuthenticated,]
    

    def get_serializer_class(self):
        if self.action == 'list' and self.request.user.year>2:
            return RoundInfoSerializer
        elif self.action == 'retrieve' and self.request.user.year>2:
            return RoundInfoSerializer
        elif self.action == 'list' and self.request.user.year<3:
            return RoundInfoJuniorSerializer
        elif self.action == 'retrieve'and self.request.user.year<3:
            return RoundInfoJuniorSerializer
        return RoundInfoDefaultSerializer
    def get(self):
        objects = Round_Info.objects.all()
        Serializer = get_serializer_class(self)
        valid_pks= []  # # storage for keys of valid objects
        # permissions: List[drf_permissions.BasePermission] = self.get_permissions()
        for object in objects:
            if FullAccessRoundMarksPermission.has_object_permission(self,request, object):
                valid_pks.append(object.pk)
        filtered_objects=Round_Info.objects.filter(pk__in=valid_pks)
        serializer=Serializer(filtered_objects)
        return Response(serializer.data)

    
    def create(self, request, format=None):
        serializer = RoundInfoDefaultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            section_objects=Section.objects.filter(round=request.data['round'])
            section_serializer=SectionDefaultSerializer(section_objects,many=True)
            for section in section_serializer.data:
                sectional_marks_serializer=SectionalMarksDefaultSerializer(data={
                'student':request.data['student'],
                'section':section['id'],
                'marks':0
                })
                if sectional_marks_serializer.is_valid():
                    sectional_marks_serializer.save()
                question_objects=Question.objects.filter(section=section['id'])
                question_serializer=QuestionDefaultSerializer(question_objects,many=True)
                for question in question_serializer.data:
                    question_status_serializer =QuestionStatusDefaultSerializer(data={
                        'question':question['id'],
                        'student':request.data['student'],
                        'marks':0
                    })
                    if question_status_serializer.is_valid():
                        question_status_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            for data in request.data:
                section_objects=Section.objects.filter(round=data['round'])
                section_serializer=SectionDefaultSerializer(section_objects,many=True)
                for section in section_serializer.data:
                    sectional_marks_serializer=SectionalMarksDefaultSerializer(data={
                    'student':data['student'],
                    'section':section['id'],
                    'marks':None
                    })
                    if sectional_marks_serializer.is_valid():
                        sectional_marks_serializer.save()
                    question_objects=Question.objects.filter(section=section['id'])
                    question_serializer=QuestionDefaultSerializer(question_objects,many=True)
                    for question in question_serializer.data:
                        question_status_serializer =QuestionStatusDefaultSerializer(data={
                        'question':question['id'],
                        'student':data['student'],
                        'marks':None
                        })
                        if question_status_serializer.is_valid():
                            question_status_serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)


    @action(methods=['GET'],detail=False,url_name='get_marks_by_round',url_path='get_marks_by_round/(?P<round_id>\d+)')
    def get_marks_by_round(self,request,round_id):
        filter_field=self.request.query_params.get('filter-field')
        percent=int(self.request.query_params.get('percent'))
        finalData =[]
        round_objects = Round_Info.objects.filter(round=round_id).order_by("student")
        
        valid_pks= [] 
        for object in round_objects:
            object.marks_obtained
            if FullAccessRoundMarksPermission.has_object_permission(self,request, object):
                valid_pks.append(object.pk)

        round_filtered_objects=Round_Info.objects.filter(pk__in=valid_pks)  
        count = round_filtered_objects.count()
        required_students=math.floor((percent*count)/100)
        if filter_field=='total_marks':
            round_pfiltered_objects=Round_Info.objects.filter(pk__in=valid_pks).order_by('-_marks_obtained')[:required_students]
        else:
            round_pfiltered_objects = round_filtered_objects
        
        round_data = RoundInfoSerializer(round_pfiltered_objects, many=True)
        for round in round_data.data:
            section_data={}
            sectional_marks=Sectional_Marks.objects.filter(section__round=round_id, student=round['student']['id'])
            include=True
            sectionSerializer=SectionalMarksSerializer(sectional_marks,many=True)
            section_data['id']=round['id']
            section_data['student_name']=round['student']['name']
            section_data['student_id']=round['student']['id']
            section_data['total_marks']=round['_marks_obtained']
            
            for section in sectionSerializer.data:
                print(section['id'])
                question_objects=Question_Status.objects.filter(question__section=section['section']['id'], student=section['student']['id'])
                question_data=QuestionStatusSerializer(question_objects,many=True)
                section_data[section['section']['name']]=section['marks']
                if filter_field==section['section']['name']:
                    sectional_marks_objects=Sectional_Marks.objects.filter(section=section['section']['id']).order_by('-marks')[:required_students]
                    sectional_marks_pserializer=SectionalMarksDefaultSerializer(sectional_marks_objects,many=True)
                    include=False
                    print(sectional_marks_pserializer.data)
                    for sectional_pmark in sectional_marks_pserializer.data:
                        if section['id']==sectional_pmark['id']:
                            include=True

                for question in question_data.data:
                    section_data[question['question']['id']]=question['marks']
                    if filter_field==question['question']['id']:
                        question_marks_objects=Question_Status.objects.filter(question=question['question']['id']).order_by('-marks')[:required_students]
                        question_marks_pserializer=QuestionStatusSerializer(question_marks_objects,many=True)
                        include=False
                        print(question_marks_pserializer.data)
                        for question_pmark in question_marks_pserializer.data:
                            if question['id']==question_pmark['id']:
                                include=True

            if include==True:
                finalData.append(section_data)
            

        return Response(finalData)
    

    @action(methods=['GET'],detail=False,url_name='get_projects_by_round',url_path='get_projects_by_round/(?P<round_id>\d+)')
    def get_projects_by_round(self,request,round_id):
        finalData =[]
        round_objects = Round_Info.objects.filter(round=round_id)
        valid_pks= [] 
        for object in round_objects:
            object.marks_obtained
            if FullAccessRoundMarksPermission.has_object_permission(self,request, object):
                valid_pks.append(object.pk)

        round_filtered_objects=Round_Info.objects.filter(pk__in=valid_pks)
        round_data = RoundInfoSerializer(round_filtered_objects, many=True)
        for round in round_data.data:
            section_data={}
            sectional_marks=Sectional_Marks.objects.filter(section__round=round_id, student=round['student']['id'])
            sectionSerializer=SectionalMarksSerializer(sectional_marks,many=True)
            section_data['id']=round['id']
            section_data['student_name']=round['student']['name']
            section_data['student_id']=round['student']['id']
            section_data['submission_link']=round['submission_link']
            if round['panel'] is not None:
                section_data['panel']=round['panel']['location']
            section_data['total_marks']=round['_marks_obtained']
            for section in sectionSerializer.data:
                section_data[section['section']['name']]=section['marks']
            finalData.append(section_data)
            

        return Response(finalData)


    def update(self,request,pk,*args,**kwargs):
        object = Round_Info.objects.get(pk=pk)
        serializer=RoundInfoDefaultSerializer(object,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("wrong parameters")
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        'Panel',
        {
        'type':'echo_message',
        'message': 'Comment Changed'
        }
)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        round_info_serializer=RoundInfoDefaultSerializer(instance)
        round_id=round_info_serializer.data['round']
        student_id=round_info_serializer.data['student']
        sectional_marks_objects=Sectional_Marks.objects.filter(section__round=round_id,student=student_id)
        question_status_objects=Question_Status.objects.filter(question__section__round=round_id,student=student_id)
        sectional_marks_objects.delete()
        question_status_objects.delete()
        instance.delete()

        return Response(data='successfully deleted')