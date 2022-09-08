from tkinter import CASCADE
from django.db import models
from round import Round
from candidate import Candidate
from interview_panel import Interview_Panel


class Round_Info(models.Model):
    student = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    duration = models.DurationField()
    marks_obtained = models.IntegerField()
    remarks = models.TextField()
    panel = models.ForeignKey(Interview_Panel,on_delete=models.DO_NOTHING)
    
