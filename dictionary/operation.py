import sqlite3
import random

def query_db(query):
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     cursor.execute(f"{query}")
     result = cursor.fetchall()
     return (result)

def get_random():
     words = query_db("SELECT * FROM words")
     a = random.randint(0, len(words))
     return words[a]

def select_word(query):
     word = query_db(f"SELECT * FROM words WHERE word == '{query}'")
     i = 1
     if len(word) > 1:
          while i < len(word):
               word[0] = list(word[0])
               word[0][4] = word[0][4] + " also " + word[i][4]
               i+=1
     elif len(word) < 1:
          return "Not Found"
     return word[0]
