from rest_framework import viewsets
from mainapp.models import Sectional_Marks
from mainapp.serializers import SectionalMarksSerializer

class SectionalMarksViewSet(viewsets.ModelViewSet):

    queryset=Sectional_Marks.objects.all()
    serializer_class=SectionalMarksSerializer