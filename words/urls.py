from django.urls import path
from django.conf.urls import url
from . import views

app_name = "words"

urlpatterns = [
    path("wordlist/", views.word_list, name="list"),
    path("create/", views.word_create, name="create"),
    path("learn/", views.learn_word, name="learn"),
    path("practice/", views.practice_word, name="practice"),
    url(r'^(?P<slug>[\w-]+)/$', views.word_detail, name="detail"),
]
