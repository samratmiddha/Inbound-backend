from django.db import models


class Chats(models.Model):
   message=models.TextField()
   sender=models.ForeignKey('User',related_name='user_messages',on_delete=models.CASCADE)
   time=models.DateTimeField(auto_now_add=True)
   panel=models.ForeignKey('Interview_Panel',on_delete=models.CASCADE,blank=True,null=True)

   def __str__(self):
    return f"{self.sender}"
    
