from email.policy import default
from django.db import models

CANDIDATE_FROM_CHOICES = [
    ('P', 'Project'),
    ('T', 'Test'),
    ('O', 'Other'),
]


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True, null=True)
    branch = models.CharField(max_length=200, blank=True, null=True)
    mobile_no = models.CharField(max_length=14, blank=True, null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    CG = models.FloatField(blank=True, null=True)
    year = models.IntegerField(default=1)
    enrollment_number = models.CharField(max_length=8, blank=True, null=True)

    candidate_from = models.CharField(
        max_length=1, choices=CANDIDATE_FROM_CHOICES)

    rounds = models.ManyToManyField(
        'Round', through='Round_Info')
