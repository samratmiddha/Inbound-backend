
from django.db import models


class Round_Info(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='round_student_info')
    round = models.ForeignKey('Round', on_delete=models.CASCADE,related_name='round_info')
    time_start = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    marks_obtained = models.IntegerField(default=0, blank=True)
    remarks = models.TextField(blank=True, null=True)
    panel = models.ForeignKey('Interview_Panel', on_delete=models.RESTRICT,blank=True,null=True,related_name='round_panel')

class Meta:
    verbose_name_plural='Round_Info'
    verbose_name='Round_Info'

def __str__(self):
    return f"{self.student}-{self.round}"