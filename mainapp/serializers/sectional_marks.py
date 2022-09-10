
from rest_framework import serializers
from mainapp.models import Sectional_Marks
class SectionalMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sectional_Marks
        fields='__all__'
