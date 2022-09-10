
from django.db import models


class InfoToConvey(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    information = models.CharField(max_length=500)
    is_exterminated = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
    is_conveyed = models.BooleanField(default=False)
