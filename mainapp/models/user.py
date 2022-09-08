
from django.db import models

ROLE_CHOICES = [
    ('designer', 'Designer'),
    ('developer', 'Developer'),
]


class User(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=254)
