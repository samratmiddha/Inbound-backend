from django.db import models
from mainapp.constants import PANEL_TYPE_CHOICES



class Interview_Panel(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE,related_name='panel_season')
    members = models.ManyToManyField('User',related_name='panel_members')
    is_active = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    type=models.CharField(max_length=4,choices=PANEL_TYPE_CHOICES,null=True)
    current_student=models.ForeignKey('Candidate',on_delete=models.CASCADE,null=True,blank=True)

    
    class Meta:
        verbose_name_plural='Interview_Panels'

    def __str__(self):
        return f"{self.location}"
