from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=30)
    definition = models.TextField
    origins = models.CharField(max_length=30)
    context = models.TextField
    word_type = models.CharField(max_length=10)

    def __str__(self):
        return self.word