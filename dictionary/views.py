from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import operation
import sqlite3
from .models import Reaction

# Create your views here.
def index(request):
     data = operation.get_random()
     try:
          word_up = Reaction.objects.get(word=data[1]).upvote
          word_down = Reaction.objects.get(word=data[1]).downvote
     except:
          word_down = 0
          word_up = 0
     
     return render(request, "index.html", {
          "word": data[1],
          "type": data[2],
          "definition": data[4],
          "title": "Discover Words",
          "upvote": word_up,
          "downvote": word_down})

def word(request, word):
     data = operation.select_word(word.lower())
     try:
          word_up = Reaction.objects.get(word=data[1]).upvote
          word_down = Reaction.objects.get(word=data[1]).downvote
     except:
          word_down = 0
          word_up = 0
          pass
     if data == "Not Found":
          return render(request, "index.html", {"data": data, "title": data})
     return render(request, "index.html", {
          "word": data[1],
          "type": data[2],
          "definition": data[4],
          "title": data[1],
          "upvote": word_up,
          "downvote": word_down})

def upvote(request, word):
     try:
          react = Reaction.objects.get(word=word)
          react.upvote+=1
          react.save()
          return HttpResponse("saved")
     except:
          react = Reaction(word=word, upvote=1, downvote=0)
          react.save()
          return HttpResponse("saved")

def downvote(request, word):
     try:
          react = Reaction.objects.get(word=word)
          react.downvote+=1
          react.save()
          return HttpResponse("saved")
     except:
          react = Reaction(word=word, upvote=0, downvote=1)
          react.save()
          return HttpResponse("saved")

def search(request):
     word = request.GET["search"]
     return redirect(f"/word/{word}")