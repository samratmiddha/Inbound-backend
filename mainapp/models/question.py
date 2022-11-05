from django.db import models


class Question(models.Model):
    question_name = models.TextField()
    question_text = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.CASCADE,related_name='question_section')
    asignee = models.ManyToManyField('User',related_name='question_asignees',blank=True)

    class Meta:
        verbose_name_plural='question'

    def __str__(self):
        return f"{self.question_name}"

    
