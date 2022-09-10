from django.db import models


class Question_Status(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    marks = models.IntegerField(blank=True, null=True)
    normalized_marks = models.FloatField(default=marks)
    is_checked = models.BooleanField(default=False)
