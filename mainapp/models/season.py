from django.db import models
from mainapp.constants import  ROLE_CHOICES
import datetime


class Season(models.Model):
    name = models.CharField(max_length=200)
    session = models.IntegerField(default=datetime.date.today().year)
    season_type = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_ongoing = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Seasons'

    def __str__(self):
        return self.name