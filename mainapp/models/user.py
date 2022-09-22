
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

ROLE_CHOICES = [
    ('designer', 'Designer'),
    ('developer', 'Developer'),
]


class User(AbstractUser):
    username = models.CharField(max_length=200,unique=True,primary_key=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    year = models.IntegerField(null=True,blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    enrolment_number = models.CharField(max_length=8,)
    USERNAME_FIELD = 'username'


    class Meta:
        verbose_name_plural='Users'

