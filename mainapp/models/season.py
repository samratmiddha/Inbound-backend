from django.db import models
from .user import User, ROLE_CHOICES
import datetime


class Season(models.Model):
    name = models.CharField(max_length=200)
    session = models.IntegerField(default=datetime.date.today().year)
    season_type = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_ongoing = models.BooleanField(default=True)
