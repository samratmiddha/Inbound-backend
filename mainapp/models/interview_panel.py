

from django.db import models

from django.contrib.postgres.fields import ArrayField

PANEL_TYPE_CHOICES=[
    ('tech','Tech'),
    ('hr','HR'),
]


class Interview_Panel(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    members = models.ManyToManyField('User')
    is_active = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    type=models.CharField(max_length=4,choices=PANEL_TYPE_CHOICES,null=True)

    
    class Meta:
        verbose_name_plural='Interview_Panels'

    def __str__(self):
        return f"{self.location}"
