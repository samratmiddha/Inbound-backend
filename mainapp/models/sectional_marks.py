from tkinter import CASCADE
from django.db import models
from section import Section
from candidate import Candidate


class Sectional_Marks(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    student = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
