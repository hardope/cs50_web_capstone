# CS50-Web-capstone

Cs50 web Final project

## Dictionary

This is a single page online dictonary we application used for searching words.
### Languages Used In Development
* python
* Django
* JavaScript
* CSS
* SQLite3

### details:
on loading the default page a random word is selected and displayed alongside its definition and word type. This is achieved by calling some functions from the operations.py file, a word is returned along side its meaning and definition, The word is then passed Into the Html file using Jinja templating engine.<br>

The Search textbox is used to find words. After The search button is filled and a request is sent to the server, the view in question fetches the user input and redirects to the view word route<br>

There's also the Upvote and Downvote button which calls respective javascript functions to send a request to update the server data. The purpose of this function is to enable users to tell if a definition is correct or not depending on the ratio of upvote to downvotes provided by people who previously viewed the words and its definition

# Distinctiveness and Complexity

I am convinced that my project satisfies the distinctiveness and complexity requirements because it is not similar in any way to any of the web applications we have developed so far. 

### The web applications we have developed so far:

* A Google search clone
* A project similar to wikipedia that enables us to create an article with a markdown system and edit it.
* A Bid auction website
* A SPA (single page app) - mail app
* A network App in which we can create/like a post, edit our own post and follow/unfollow other users.

## Files
* operation.py: This python file contains functions that connect to a database of over 115,000 words and runs several sqlite commands on the database

* urls.py: Contains the available urls in this project and links them to their functions for response

* advancedict.db: is the sqlite database containing all over 115,000 words

* admin.py: add the models to admin app

* templates/index.html: The html file to display words

## Installation
run the following command snipet in project root directory

``` bash
# Install Modules
~ $ pip install requirements.txt

```

``` bash
# Install Modules
~ $ python manage.py makemigrations

```

``` bash
# Install Modules
~ $ python manage.py migrate

```

``` bash
# Run server
~ $ python manage.py runserver

```

### Admin page Interface
* Username: user
* password: qwerty

#### To Create a new account for the admin interface
- Run the following command snipet

``` bash
# run command and provide your details as required
~ $ python manage.py create superuser

```

# files structure

```

/ (folder)
-- (files)

/capstone
     /__pycache__
          ...
     --__init__.py
     --asgi.py
     --settings.py
     --urls.py
     --wsgi.py
/dictionary
     /__pycache__
          ...
     /migrations
          --__init__.py
          0001_initial.py
          0002_rename_reactions_reaction.py
     /templates
          index.html
     __init__.py
     admin.py - admin
     apps.py
     models.py - models
     operation.py - required functions
     tests.py
     urls.py
     views.py
advancedict.db
db.sqlite3
manage.py
README.md
requirements.txt

```