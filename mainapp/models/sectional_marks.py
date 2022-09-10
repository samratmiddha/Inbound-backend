
from django.db import models

class Sectional_Marks(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
