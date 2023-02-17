from django.db import models
from .sectional_marks import Sectional_Marks
from ..serializers.sectional_marks import SectionalMarksDefaultSerializer

class Round_Info(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='round_student_info')
    round = models.ForeignKey('Round', on_delete=models.CASCADE,related_name='round_info')
    time_start = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    _marks_obtained = models.IntegerField(default=0, blank=True,null= True)
    remarks = models.TextField(blank=True, null=True)
    panel = models.ForeignKey('Interview_Panel', on_delete=models.CASCADE,blank=True,null=True,related_name='round_panel')
    submission_link = models.URLField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural='Round_Info'
        verbose_name='Round_Info'
        unique_together = ['student', 'round']

    def __str__(self):
        return f"{self.student}-{self.round}"



    # @property
    # def marks_obtained(self):
    #     return self._marks_obtained


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



