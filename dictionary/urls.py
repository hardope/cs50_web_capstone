from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("word/<str:word>", views.word, name="word"),
     path("search", views.search, name="word"),
     path("upvote/<str:word>", views.upvote, name="upvote"),
     path("downvote/<str:word>", views.downvote, name="downvote"),
]