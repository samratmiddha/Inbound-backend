
from tabnanny import verbose
from django.db import models
from django.contrib.postgres.fields import ArrayField


ROUND_TYPE_CHOICES = [
    ('I', 'Interview'),
    ('P', 'Project'),
    ('T', 'Test'),
]


class Round(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ROUND_TYPE_CHOICES)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    dates = ArrayField(
        models.DateField(),
        blank=True
    )

    class Meta:
        verbose_name_plural='Rounds'

    def __str__(self):
        return self.name