from django.db import models


class Question_Status(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE,related_name='question_info')
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='question_student_info')
    marks = models.IntegerField(default=0,blank=True, null=True)
    normalized_marks = models.FloatField(default=marks,blank=True)
    is_checked = models.BooleanField(default=False)
    submission_link = models.URLField(max_length=300, blank=True, null=True)
    class Meta:
        verbose_name_plural='Question_Status'

    def __str__(self):
        return f"{self.student}-{self.question}"
