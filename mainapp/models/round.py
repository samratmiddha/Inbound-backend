from django.db import models
from mainapp.constants import ROUND_TYPE_CHOICES




class Round(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ROUND_TYPE_CHOICES)
    season = models.ForeignKey('Season', on_delete=models.CASCADE,related_name='round_season')
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)

    class Meta:
        verbose_name_plural='Rounds'

    def __str__(self):
        return self.name