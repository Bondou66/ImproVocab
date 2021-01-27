from django.shortcuts import render
from .models import Word
from django.http import HttpResponse

def word_list(request):
    words = Word.objects.all().order_by('word')
    return render(request, "words/word_list.html", {'words' : words})

def word_detail(request, slug):
    word = Word.objects.get(slug=slug)
    return render(request, "words/word_detail.html", {'word' : word })