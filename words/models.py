from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=30)
    definition = models.TextField()
    origins = models.CharField(max_length=30)
    context = models.TextField()
    word_type = models.CharField(max_length=10)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.word

    def snippet(self):
        if len(self.definition) > 50:
            return self.definition[:50] + "..."
        else:
            return self.definition

class Learned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("user", "word"),)
    
    def __str__(self):
        return self.word.word
