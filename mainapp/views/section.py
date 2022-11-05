from rest_framework import viewsets
from mainapp.models import Section
from mainapp.models import Question
from mainapp.serializers import SectionSerializer
from mainapp.serializers import QuestionDefualtSerializer
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
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return SectionSerializer
        if self.action == 'retrieve':
            return SectionSerializer
        return SectionDefaultSerializer
 
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
        columns.append({'field':'id' ,'headerName':'Id','flex':5})
        columns.append({'field':'student_name' ,'headerName':'Name','flex':15})
        columns.append({'field':'student_id' ,'headerName':'SID','flex':10})
        groups.append({'groupId':'internal','headerName':'Internal','children':[{'field':'id'},{'field':'student_id'},{'field':'student_name'},{'field':'total_marks'}]})
        columns.append({'field':'total_marks' ,'headerName':'Total','flex':10})
        objects =Section.objects.filter(round=round_id)
        section_data=SectionDefaultSerializer(objects,many=True)
        for section in section_data.data:
            print('jjj')
            group={}
            children=[]
            columns.append({'field':section['name'] ,'headerName':section['name'],'flex':10})
           
            group['groupId']=section['id']
            group['headerName']=section['name']
            question_objects=Question.objects.filter(section=section['id'])
            question_data =QuestionDefualtSerializer(question_objects,many=True)
            children.append({'field':section['name']})
            for question in question_data.data:
                columns.append({'field':question['id'] ,'headerName':question['question_name'],'flex':10})
                question_fields={}
                question_fields['field']=question['id']
                children.append(question_fields)
            group['children']=children
            groups.append(group)
        finalData['groups']=groups
        finalData['columns']=columns

        return Response(finalData)



