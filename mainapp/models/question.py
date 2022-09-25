from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    submission_link = models.URLField(max_length=300, blank=True, null=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE,related_name='question_section')
    asignee = models.ManyToManyField('User',related_name='question_asignees')

    class Meta:
        verbose_name_plural='question'

    def __str__(self):
        return f"{self.question_text}"

    
