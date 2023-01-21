from django.db import models

# Create your models here.
class Reaction(models.Model):
     word = models.CharField(max_length=70)
     upvote = models.IntegerField()
     downvote = models.IntegerField()

     def __str__(self):
          return f"{self.word}: Upvote: {self.upvote}, Downvote: {self.downvote}"
