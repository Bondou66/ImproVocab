from django.shortcuts import render
from .models import Word
from django.contrib.auth.decorators import login_required

def word_list(request):
    words = Word.objects.all().order_by('word')
    return render(request, "words/word_list.html", {'words' : words})

def word_detail(request, slug):
    word = Word.objects.get(slug=slug)
    return render(request, "words/word_detail.html", {'word' : word })

@login_required(login_url="/accounts/login/")
def word_create(request):
    return render(request, "words/word_create.html")