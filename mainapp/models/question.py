
from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    submission_link = models.URLField(max_length=300, blank=True, null=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    asignee = models.ManyToManyField('User', on_delete=models.SET_NULL)
