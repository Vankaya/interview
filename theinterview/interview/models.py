from django.db import models

# Create your models here.

class QuestionAnswer(models.Model):
    quest = models.CharField(max_length=1000)
    answ = models.CharField(max_length=1000)
