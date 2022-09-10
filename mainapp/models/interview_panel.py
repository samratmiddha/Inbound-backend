
from django.db import models

from django.contrib.postgres.fields import ArrayField


class Interview_Panel(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    members = models.ManyToManyField('User')
    is_active = models.BooleanField(default=False)
    location = models.CharField(max_length=200)

    custom_questions = ArrayField(
        models.TextField(),
        blank=True
    )
