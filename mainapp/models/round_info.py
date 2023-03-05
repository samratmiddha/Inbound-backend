from django.db import models
from .sectional_marks import Sectional_Marks
from ..serializers.sectional_marks import SectionalMarksDefaultSerializer
import math
from rest_framework import serializers



class Round_Info(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='round_student_info')
    round = models.ForeignKey('Round', on_delete=models.CASCADE,related_name='round_info')
    time_start = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    _marks_obtained = models.IntegerField(default=0, blank=True,null= True)
    remarks = models.TextField(blank=True, null=True)
    panel = models.ForeignKey('Interview_Panel', on_delete=models.CASCADE,blank=True,null=True,related_name='round_panel')
    submission_link = models.URLField(max_length=300, blank=True, null=True)
    normalized_marks=models.FloatField(blank=True,null=True)

    class Meta:
        verbose_name_plural='Round_Info'
        verbose_name='Round_Info'
        unique_together = ['student', 'round']

    def __str__(self):
        return f"{self.student}-{self.round}"



    @property
    def normalize(self):
        standard_deviation_intermediate=0
        standard_deviation =1
        queryset2= Round_Info.objects.filter(round=self.round)
        serializer2 = RoundInfoDefaultSerializer(queryset2,many=True)
        count=0
        total_round_marks=0
        for obj in serializer2.data:
            if obj['_marks_obtained']!= None:
                total_round_marks+=obj['_marks_obtained']
                count+=1
        if count!=0:
            average=total_round_marks/count
        else:
            average=self._marks_obtained
        for obj in serializer2.data:
            if obj['_marks_obtained']!= None:
                standard_deviation_intermediate+=((obj['_marks_obtained']-average)*(obj['_marks_obtained']-average))
        if count!=0:
            standard_deviation = math.sqrt(standard_deviation_intermediate/count)
        if standard_deviation!=0 and self._marks_obtained!=None:
            self.normalized_marks=float((self._marks_obtained-average)/standard_deviation)
        else:
            self.normalized_marks=0
        self.save()



    @property
    def marks_obtained(self):
        queryset=Sectional_Marks.objects.filter(student=self.student,section__round=self.round)
        serializer=SectionalMarksDefaultSerializer(queryset,many=True)
        total_marks=0
        for section_info in serializer.data:
            if(section_info['marks']!=None):
                total_marks+=section_info['marks']
        self._marks_obtained=total_marks
        self.save()

        print('bbb')
        print(total_marks)
        return total_marks


class RoundInfoDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round_Info
        fields = '__all__'

