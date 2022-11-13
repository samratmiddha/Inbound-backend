from django.db import models
from .question_status import Question_Status
from ..serializers.question_status import QuestionStatusDefaultSerializer
class Sectional_Marks(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE,related_name='marks_section')
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='sectional_marks_student')
    marks = models.IntegerField(null=True,blank =True)

    class Meta:
        verbose_name_plural='Sectional_marks'

    def __str__(self):
        return f"{self.section}-{self.student}"


    @property
    def sectional_marks(self):
        queryset=Question_Status.objects.filter(question__section=self.section,student=self.student)
        serializer=QuestionStatusDefaultSerializer(queryset,many=True)
        total_marks=0
        for question_info in serializer.data:
            total_marks+=question_info['marks']
        self.marks=total_marks
        self.save()
