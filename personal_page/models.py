from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DirectMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False) 


    def __str__(self):
        return f'From: {self.sender.username}, To: {self.recipient.username}, Time: {self.created_at}'