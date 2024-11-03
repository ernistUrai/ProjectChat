from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField('Ваше имя', max_length=100)
    content = models.TextField('Собшение')
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.user