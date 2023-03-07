from django.db import models

class Chats(models.Model):
    fron = models.IntegerField()
    to = models.IntegerField()
    message = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)