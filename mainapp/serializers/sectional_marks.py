
from rest_framework import serializers
from .candidate import CandidateNameSerializer
from .section import SectionNameSerializer
from ..models.sectional_marks import Sectional_Marks
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class SectionalMarksSerializer(serializers.ModelSerializer):
    student = CandidateNameSerializer()
    section = SectionNameSerializer()

    class Meta:
        model = Sectional_Marks
        fields = '__all__'


class SectionalMarksDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectional_Marks
        fields = '__all__'
