from rest_framework import viewsets
from mainapp.models import Round_Info
from mainapp.models import Section
from mainapp.models import Sectional_Marks
from mainapp.models import Question_Status
from mainapp.serializers import RoundInfoSerializer
from mainapp.serializers import RoundInfoDefaultSerializer
from mainapp.serializers import SectionalMarksSerializer
from mainapp.serializers import QuestionStatusSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404


class RoundInfoViewSet(viewsets.ModelViewSet):
    queryset = Round_Info.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['student', 'round', 'panel','marks_obtained']
    filterset_fields = ['student', 'round', 'panel']
    ordering = ['-marks_obtained']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RoundInfoSerializer
        if self.action == 'retrieve':
            return RoundInfoSerializer
        return RoundInfoDefaultSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(RoundInfoDefaultSerializer(instance.parent).data)
 

    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    @action(methods=['GET'],detail=False,url_name='get_marks_by_round',url_path='get_marks_by_round/(?P<round_id>\d+)')
    def get_marks_by_round(self,request,round_id):
        # channel_layer=get_channel_layer()
        # channel_layer.group_send('IMG',{"msg":'bum bum'})
        finalData =[]
        round_objects = Round_Info.objects.filter(round=round_id)
        round_data = RoundInfoSerializer(round_objects, many=True)

        print(request.user)
        for round in round_data.data:
            section_data={}
            sectional_marks=Sectional_Marks.objects.filter(section__round=round_id, student=round['student']['id'])
            sectionSerializer=SectionalMarksSerializer(sectional_marks,many=True)
            section_data['id']=round['id']
            section_data['student_name']=round['student']['name']
            section_data['student_id']=round['student']['id']
            section_data['total_marks']=round['marks_obtained']
            for section in sectionSerializer.data:
                print(section['id'])
                question_objects=Question_Status.objects.filter(question__section=section['section']['id'], student=section['student']['id'])
                question_data=QuestionStatusSerializer(question_objects,many=True)
                section_data[section['section']['name']]=section['marks']
                for question in question_data.data:
                    section_data[question['question']['id']]=question['marks']
            finalData.append(section_data)
            

        return Response(finalData)
