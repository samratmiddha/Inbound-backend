from django.db import models



class Section(models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE,related_name='section_round')
    max_marks = models.IntegerField(blank=True,null=True)
    weightage = models.IntegerField(default=1, blank=True)
    name = models.CharField(max_length=200)
    number_of_questions=models.IntegerField(default=0,blank=True)

    class Meta:
        verbose_name_plural='Sections'

    def __str__(self):
        return self.name
