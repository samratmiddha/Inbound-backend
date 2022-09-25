from django.db import models

class Sectional_Marks(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE,related_name='marks_section')
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='sectional_marks_student')
    marks = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural='Sectional_marks'

    def __str__(self):
        return f"{self.section}-{self.student}"
