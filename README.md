# CS50-Web-capstone Project By Opeouwa Adeyeri

Cs50 web Final project

---

## About

This project is a single page web application used to check word definition and type. This project makes use of SQLite3 Database management system to store a dictionary of over 115,000 words and also makes use of The default Django Models to store the upvotes and downvotes.

---

### Languages Used In Development
* python
* Django
* JavaScript
* CSS
* SQLite3

---

# Distinctiveness and Complexity

I am convinced that my project satisfies the distinctiveness requirements because it is not similar in any way to any of the web applications we have developed so far.<br>

I believe this project satisfies the complexity requiment for several reasons. One of the requirements states that the project must utilize Django (using at least One model) on the back-end and JavaScript on the front-end, This requirement is met as I used the Django Framework and used the Reaction Model to store the upvotes and downvotes for each word in the dictionary. Also JavaScript is used on the front-end to send an Http request to the backend to update the upvote or downvote and edit the values displayed on the pages in respect to the button clicked.

---

### The web applications Developed During Cs50WEB:

* A Google search clone
* A project similar to wikipedia that enables us to create an article with a markdown system and edit it.
* A Bid auction website
* A SPA (single page app) - mail app
* A network App in which we can create/like a post, edit our own post and follow/unfollow other users.

---

### Details & usage:
on loading the default page a random word is selected and displayed alongside its definition and word type. This is achieved by calling some functions from the operations.py file, a word is returned along side its meaning and definition, This word is then passed Into the Html file using Jinja templating engine.<br>

The Search textbox is used to find words. After The search button is filled and a request is sent to the server, the view in question fetches the user input and redirects to the view word route<br>

There's also the Upvote and Downvote button which calls respective javascript functions to send a request to update the server data. The purpose of this function is to enable users to tell if a definition is correct or not depending on the ratio of upvote to downvotes provided by people who previously viewed the words and its definition.

---

The following is the file structure of the project where I added or modified. Default project files are ommitted.

```
/ (folder)
-- (files)

/Capstone - main project folder
 --README.md - this file
 --requirements.txt - list of libraries needed to run
 --advancedict.db - SQLite database to store all words and definition
 --db.sqlite - SQLite database used by Django to store data in models
  /Capstone - Django main project folder
   --settings.py - slightly modified settings
   --urls.py - path configuration
  /dictionary - Django Dictionary App
   /templates
     -index.html - html page for dictionary
   /static
     -index.js - Javascript for front end
     -styles.css - stylesheet
   --admin.py - admin settings for model view
   --operation.py - Functions to run sqlite3 commands and return required Data
   --models.py - database models
   --urls.py - all standard HTTP request routing handled here
   --views.py - code to handle each view
```

---

<br>

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
### Video Demo
[Youtube](https://www.youtube.com/watch?v=YAWSxCcllsw)
