from django.db import models


class InfoToConvey(models.Model):
    season = models.ForeignKey('Season',on_delete=models.CASCADE)
    student = models.ForeignKey('Candidate', on_delete=models.CASCADE,related_name='student_info')
    information = models.CharField(max_length=500)
    remarks = models.TextField(blank=True, null=True)
    is_conveyed = models.BooleanField(default=False)
    round_info = models.ForeignKey('Round_Info',on_delete=models.CASCADE,blank=True)

    class Meta:
        verbose_name_plural='InfoToConvey'

    def __str__(self):
        return f"{self.student}-{self.information}"
