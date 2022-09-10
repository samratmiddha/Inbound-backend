
from django.db import models


class Round_Info(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    time_start = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    marks_obtained = models.IntegerField(default=0, blank=True)
    remarks = models.TextField(blank=True, null=True)
    panel = models.ForeignKey('Interview_Panel', on_delete=models.RESTRICT)
