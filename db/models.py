from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=15, unique=True)
    translation = models.TextField()
    api = models.TextField()
