from django.shortcuts import render, redirect
from .models import Word, Learned
from django.contrib.auth.decorators import login_required
from . import forms

def word_list(request):
    words = Word.objects.all().order_by('word')
    return render(request, "words/word_list.html", {'words' : words})

def word_detail(request, slug):
    word = Word.objects.get(slug=slug)
    return render(request, "words/word_detail.html", {'word' : word })

@login_required(login_url="/accounts/login/")
def word_create(request):
    if request.method == 'POST':
        form = forms.CreateWordForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            learned = Learned()
            learned.user = request.user
            learned.word = instance
            instance.save()
            return redirect('words:list')
    else:
        form = forms.CreateWordForm()
    return render(request, "words/word_create.html", {'form' : form})