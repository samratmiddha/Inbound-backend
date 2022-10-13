
from rest_framework import serializers
from mainapp.serializers.candidate import CandidateNameSerializer
from mainapp.serializers.section import SectionNameSerializer
from mainapp.models import Sectional_Marks


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
