from django.db import models
from question import Question
from candidate import Candidate

class Question_Status:
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    student= models.ForeignKey(Candidate,on_delete=models.CASCADE)
    marks= models.IntegerField()
    normalized_marks=models.FloatField()
    is_checked=models.BooleanField(default=False)
    