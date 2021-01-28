from django.shortcuts import render, redirect
from .models import Word, Learned
from django.contrib.auth.decorators import login_required
from . import forms
import random

def word_list(request):
    words = Word.objects.all().order_by('word_type', 'word')
    return render(request, "words/word_list.html", {'words' : words})

def word_detail(request, slug):
    word = Word.objects.get(slug=slug)
    return render(request, "words/word_detail.html", {'word' : word})

@login_required(login_url="/accounts/login/")
def learn_word(request, slug=None):
    user = request.user
    if slug != None:
        word = Word.objects.get(slug=request.POST.get('slug'))
    else:
        learned_words = Learned.objects.values_list('word', flat=True).filter(user=user)
        words = Word.objects.exclude(id__in=learned_words)
        word = random.choice(words)
    learned = Learned()
    learned.user = user
    learned.word = word
    is_learned = Learned.objects.filter(user=user, word=word)
    if learned not in is_learned:
        learned.save()
    return render(request, "words/learn_word.html", {'word' : word})

@login_required(login_url="/accounts/login/")
def practice_word(request):
    user = request.user

    learned_words = Learned.objects.filter(user=user)
    return render(request, "words/practice_word.html", {'learned_words' : learned_words})

@login_required(login_url="/accounts/login/")
def word_create(request):
    if request.method == 'POST':
        form = forms.CreateWordForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            learned = Learned()
            learned.user = request.user
            learned.word = instance
            instance.word_type = instance.word_type.lower()
            instance.save()
            learned.save()
            return redirect('words:list')
    else:
        form = forms.CreateWordForm()
    return render(request, "words/word_create.html", {'form' : form})