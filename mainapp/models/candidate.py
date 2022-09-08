from django.db import models
from season import Season
from round import Round

CANDIDATE_FROM_CHOICES = [
    ('P', 'Project'),
    ('T', 'Test'),
    ('O', 'Other'),
]


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    branch = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=14)
    season = models.ForeignKey(Season)
    candidate_from = models.CharField(
        max_length=1, choices=CANDIDATE_FROM_CHOICES)
    CG = models.FloatField()
    year = models.IntegerChoices()
    current_round = models.ForeignKey(Round)
    enrollment_number = models.CharField(max_length=8)
