from rest_framework import viewsets
from mainapp.models import Candidate
from mainapp.serializers import CandidateSerializer
from mainapp.serializers import CandidateDefaultSerializer
from mainapp.serializers import CSVFileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import csv
import codecs
from rest_framework.response import Response
from rest_framework import  status
import io
import pandas



class CandidiateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'email', 'branch', 'enrollment_number','season']
    filterset_fields = ['name', 'email', 'branch', 'enrollment_number','season']
    ordering = ['name']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return CandidateSerializer
        if self.action == 'retrieve':
            return CandidateSerializer
        return CandidateDefaultSerializer

    @action( methods=['POST'],detail=False ,url_name='upload_data_through_file/')
    def upload_data_through_file(self, request,*args,**kwargs):
        print(self.request.data)
        serializer =  CSVFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        season_id = self.request.data['seasonId']
        csv_reader = pandas.read_csv(csv_file)
        candidate_list = []
        for _, row in csv_reader.iterrows():
            candidate_list.append(
                Candidate(
                    name=row['name'],
                    email=row['email'],
                    mobile_no=row['mobile_no'],
                    branch=row['branch'],
                    year=row['year'],
                    CG=row['CG'],
                    enrollment_number=row['enrollment_number'],
                    season_id=season_id,
                    candidate_from=row['candidate_from'],
                    is_exterminated=False,
                )
            )
        Candidate.objects.bulk_create(candidate_list)
        return Response("candidates registered successfully")


    @action(methods=['POST'],detail=False,url_name='multiple_create/')
    def multiple_create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)