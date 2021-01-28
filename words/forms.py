from django import forms
from . import models

class CreateWordForm(forms.ModelForm):
    class Meta:
        model = models.Word
        fields = ['word', 'definition', 'origins', 'context', 'word_type', 'slug', 'thumb']