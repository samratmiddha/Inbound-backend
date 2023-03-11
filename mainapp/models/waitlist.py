
from django.db import models

class Waitlist(models.Model):
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='candidate_waitlist')
    round=models.ForeignKey('Round',on_delete=models.CASCADE)
    season=models.ForeignKey('Season',on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='Candidates'

    def __str__(self):
        return f"{self.season}"

