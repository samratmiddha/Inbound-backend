from rest_framework import viewsets
from mainapp.models import Section
from mainapp.models import Question
from mainapp.models import Sectional_Marks
from mainapp.models import Round_Info
from mainapp.serializers import SectionSerializer
from mainapp.serializers import QuestionDefaultSerializer
from mainapp.serializers.round_info import RoundInfoDefaultSerializer
from mainapp.serializers.sectional_marks import SectionalMarksDefaultSerializer
from mainapp.serializers.round_info import RoundInfoSerializer
from mainapp.permissions import FullAccessPermission
from mainapp.serializers import QuestionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import SectionDefaultSerializer
from rest_framework.decorators import action
from rest_framework import  status
from rest_framework.response import Response



class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['round', 'max_marks', 'name', 'weightage']
    filterset_fields = ['round', 'max_marks', 'name', 'weightage']
    ordering = ['round']
    permission_classes = [IsAuthenticated,FullAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return SectionSerializer
        if self.action == 'retrieve':
            return SectionSerializer
        return SectionDefaultSerializer

    def create(self, request, format=None):
        serializer = SectionDefaultSerializer(data=request.data)
        print('ooo')
        if serializer.is_valid():
            instance =serializer.save()
            round_info_objects =Round_Info.objects.filter(round=request.data['round'])
            round_info_serializer= RoundInfoSerializer(round_info_objects,many=True)
            for round_info in round_info_serializer.data:
                sectional_marks_serializer=SectionalMarksDefaultSerializer(data={
                'student':round_info['student']['id'],
                'section':instance.id,
                })
                if sectional_marks_serializer.is_valid():
                    sectional_marks_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def destroy(self,request,pk,*args,**kwargs):
        instance =Section.objects.get(pk=pk)
        serializer=SectionDefaultSerializer(instance)
        instance.delete()
        print('nnnnnnnnnnnnnnnnnnnnnnnn')
        print(serializer.data)
        print('nnnnnnnnnnnnnnnnnnnnnnnn')
        section_marks_objects=Sectional_Marks.objects.filter(section__round=serializer.data['round'])
        round_info_objects=Round_Info.objects.filter(round=serializer.data['round'])
        for section_marks_object in section_marks_objects:
            section_marks_object.sectional_marks
        for round_info_object in round_info_objects:
            round_info_object.marks_obtained
        
        return Response({'msg':'successfully deleted'})
        
    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    @action(methods=['GET'],detail=False,url_name='get_section_groups',url_path='get_section_groups/(?P<round_id>\d+)')
    def get_section_groups(self,request,round_id):
        finalData={}
        groups=[]
        columns=[]
        columns.append({'field':'id' ,'headerName':'Id','flex':5,'type':'number'})
        columns.append({'field':'student_name' ,'headerName':'Name','flex':15})
        columns.append({'field':'student_id' ,'headerName':'SID','flex':10})
        groups.append({'groupId':'internal', 'headerClassName': 'my-super-theme--naming-group','headerName':'Internal','children':[{'field':'id'},{'field':'student_id'},{'field':'student_name'},{'field':'total_marks'}]})
        columns.append({'field':'total_marks' ,'headerName':'Total','flex':10,'type':'number'})
        objects =Section.objects.filter(round=round_id)
        section_data=SectionDefaultSerializer(objects,many=True)
        for section in section_data.data:
            print('jjj')
            group={}
            children=[]
            columns.append({'field':section['name'] ,'headerName':section['name'],'flex':10,'type':'number'})
           
            group['groupId']=section['id']
            group['headerName']=section['name']
            group['headerClassName']='my-super-theme--naming-group'
            question_objects=Question.objects.filter(section=section['id'])
            question_data =QuestionDefaultSerializer(question_objects,many=True)
            children.append({'field':section['name']})
            for question in question_data.data:
                columns.append({'field':question['id'] ,'headerName':question['question_name'],'flex':10 ,'editable':True,'type':'number'})
                question_fields={}
                question_fields['field']=question['id']
                children.append(question_fields)
            group['children']=children
            groups.append(group)
        finalData['groups']=groups
        finalData['columns']=columns

        return Response(finalData)


    @action(methods=['GET'],detail=False,url_name='get_project_sections',url_path='get_project_sections/(?P<round_id>\d+)')
    def get_project_sections(self,request,round_id):
        finalData={}
        columns=[]
        columns.append({'field':'id' ,'headerName':'Id','flex':5,'type':'number'})
        columns.append({'field':'student_name' ,'headerName':'Name','flex':15})
        columns.append({'field':'student_id' ,'headerName':'SID','flex':10})
        columns.append({'field':'total_marks' ,'headerName':'Total','flex':10,'type':'number'})
        columns.append({'field':'submission_link' ,'headerName':'Submission Link','flex':10,})
        columns.append({'field':'panel' ,'headerName':'Panel','flex':10,})
        objects =Section.objects.filter(round=round_id)
        section_data=SectionDefaultSerializer(objects,many=True)
        for section in section_data.data:
            print('jjj')
            columns.append({'field':section['name'] ,'headerName':section['name'],'flex':10,'type':'number','editable':True})
            
        finalData['columns']=columns

        return Response(finalData)

    

