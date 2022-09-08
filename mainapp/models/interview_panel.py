from tkinter import CASCADE
from django.db import models
from user import User
from season import Season
from django.contrib.postgres.fields import ArrayField

class Interview_Panel(models.Model):
    season=models.ForeignKey(Season,on_delete=models.CASCADE)
    members=models.ManyToManyField(User)
    custom_questions=ArrayField(
        models.TextField(),
        blank=True
    )
    is_active=models.BooleanField(default=False)
    location=models.CharField(max_length=200)
