from tkinter import CASCADE
from django.db import models



class Section(models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    max_marks = models.IntegerField(blank=True,null=True)
    Weightage = models.IntegerField(default=1, blank=True)
    name = models.CharField(max_length=200)
