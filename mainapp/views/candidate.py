from rest_framework import viewsets
from mainapp.models import Candidate
from mainapp.serializers import CandidateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import csv
import codecs
from rest_framework.response import Response

class CandidiateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields=['name','email','branch','enrolment_number']
    filterset_fields=['name','email','branch','enrolment_number']
    ordering=['name']
    permission_classes=[IsAuthenticated]


    @action(detail=False, methods=['POST'])
    def upload_data_through_file(self,request):
        file = request.FILES.get("file")
        season_id=request.POST.get("season_id")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)

        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        candidate_list=[]
        for row in serializer.data:
            candidate_list.append(
                Candidate(
                    name=row['name'],
                    email=row['email'],
                    mobile_no=row['mobile_no'],
                    branch=row['branch'],
                    year=row['year'],
                    CG=row['CG'],
                    enrolment_number=row['enrolment_number'],
                    season_id=season_id,
                    candidate_from=row['candidate_from']
                )
            )
        Candidate.objects.bulk_create(candidate_list)
        return Response("candidates registered successfully")