from django.db import models
from .question_status import Question_Status
from ..serializers.question_status import QuestionStatusDefaultSerializer
from rest_framework import serializers
import math


class Sectional_Marks(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE,related_name='marks_section')
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='sectional_marks_student')
    marks = models.IntegerField(null=True,blank =True)
    normalized_marks=models.FloatField(blank=True,null=True)
    class Meta:
        verbose_name_plural='Sectional_marks'

    def __str__(self):
        return f"{self.section}-{self.student}"


    @property
    def sectional_marks(self):
        queryset=Question_Status.objects.filter(question__section=self.section,student=self.student)
        serializer=QuestionStatusDefaultSerializer(queryset,many=True)
        total_marks=0
        for question_info in serializer.data:
            total_marks+=question_info['marks']
        print("hii0")
        self.marks=total_marks
        print("hii9")
        self.save()
        
    
    @property
    def normalize(self):
        standard_deviation_intermediate=0
        standard_deviation =1
        print("hii10")
        print("hii1")
        queryset2= Sectional_Marks.objects.filter(section=self.section)
        print("hii2")
        serializer2 = SectionalMarksDefaultSerializer(queryset2,many=True)
        print("hii3")
        count=0
        total_section_marks=0
        for obj in serializer2.data:
            if obj['marks']!= None:
                total_section_marks+=obj['marks']
                count+=1
        if count!=0:
            average=total_section_marks/count
        else:
            average=self.marks
        print("hii6")
        for obj in serializer2.data:
            if obj['marks']!= None:
                standard_deviation_intermediate+=((obj['marks']-average)*(obj['marks']-average))
        if count!=0:
            standard_deviation = math.sqrt(standard_deviation_intermediate/count)
        print("hii7")
        if standard_deviation!=0:
            self.normalized_marks=float((self.marks-average)/standard_deviation)
        else:
            self.normalized_marks=0
        print("hii4")
        self.save()
        print("hii5")



class SectionalMarksDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectional_Marks
        fields = '__all__'
















