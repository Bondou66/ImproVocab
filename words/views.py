from django.shortcuts import render, redirect
from .models import Word, Learned
from django.contrib.auth.decorators import login_required
from . import forms

def word_list(request):
    words = Word.objects.all().order_by('word_type', 'word')
    return render(request, "words/word_list.html", {'words' : words})

def word_detail(request, slug):
    word = Word.objects.get(slug=slug)
    return render(request, "words/word_detail.html", {'word' : word})

@login_required(login_url="/accounts/login/")
def learn_word(request):
    user = request.user
    learned = Learned()
    word = Word.objects.get(slug=request.POST.get('slug'))
    learned.user = user
    learned.word = word
    learned.save()
    return render(request, "words/learn_word.html")

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