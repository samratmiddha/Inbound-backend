from django.db import models


class Question_Status(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    marks = models.IntegerField(blank=True, null=True)
    normalized_marks = models.FloatField(default=marks)
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Question_Status'

    def __str__(self):
        return f"{self.student}-{self.question}"
