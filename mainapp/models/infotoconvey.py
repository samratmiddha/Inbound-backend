from tkinter import CASCADE
from django.db import models
from candidate import Candidate


class InfoToConvey(models.Model):
    student = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    information = models.CharField(max_length=500)
    is_exterminated = models.BooleanField(default=False)
    remarks = models.TextField()
    is_conveyed = models.BooleanField(default=False)
