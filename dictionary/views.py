from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import operation
from .models import Reaction

# Create your views here.

# View to display random words
def index(request):
     # call function to get random word
     data = operation.get_random()
     try:
          # Fetch Number of upvotes and downvotes
          word_up = Reaction.objects.get(word=data[1]).upvote
          word_down = Reaction.objects.get(word=data[1]).downvote
     except:
          # If not found set to 0
          word_down = 0
          word_up = 0
     
     return render(request, "index.html", {
          "word": data[1],
          "type": data[2],
          "definition": data[4],
          "title": "Discover Words",
          "upvote": word_up,
          "downvote": word_down})

# function to select and display word
def word(request, word):
     # call function to select specific word
     data = operation.select_word(word.lower())
     try:
          # Fetch Number of upvotes and downvotes
          word_up = Reaction.objects.get(word=data[1]).upvote
          word_down = Reaction.objects.get(word=data[1]).downvote
     except:
          # if not found set to 0
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

# upvote route
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

# dowmvote route
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

# Submit search value
def search(request):
     word = request.GET["search"]
     return redirect(f"/word/{word}")