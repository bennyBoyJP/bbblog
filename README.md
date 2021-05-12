# bbblog (bennyBoy's blog) - CS50's Final Project (2021)
#### Video Demo:  https://youtu.be/yMZ5CnWhVQU
#### Description:
Welcome! Thank you for checking out my blog!
It's my first one, and it was fun to make using Flask and SQLite for the database.
I dived into HTML and CSS for this project,
it was really frustrating to get the visuals working
since I had no front-end experience, but I managed
to get a basic template working using Flex. And finally deployed
Heroku!

Design:<br>
I wanted to keep things simple, so I went with a courier font to
give it an old-school kind of feeling. The green is supposed to be
reminiscent of the old monochrome screens!

Working with Flask:<br>
I think Flask is really cool, and is fun to use with Jinja. Once I
started understanding the basics of the routes, GET and POST, things started to
come together.

### Features:<br>
Phrase Generator:<br>
Previously I had worked on a random phrase generator which I never
put to use, so I used it to create random funny titles at the top of
the screen. Currently, it's set up where the user can change it by
going to the About page.

Removing Entries:<br>
The admin can delete the
last entry, or all entries, by entering the commands in the Title
box.

Dates:<br>
The dates have had (st, nd, th) suffixes concatenated to
give it a more conversational feel.

Archives:<br>
The for the visitor, the blog
shows all entries for the given month. If the user would like to
see previous entries, they can find the month/yeah in the Archive
page.

Links:<br>
Admin can post hyper links when creating entries. Because Form Textarea
is being used, hyperlinks cannot be added directly. I made a helper function in Python
to help with this using the partition method. It looks for the >>> in the entry and
breaks apart the name of the link (left side) with the hyperlink (right side). Using Jinja,
the link is posted to the bottom of the entry, using CSS to right align it. This was basically
a work around for not being able to post hyperlinks directly in the textarea.

### Summary:
This blog is not completed! I would like to incorporate Sessions
for multi-user login and security. Also I would like to add a
comment section, and go deeper into relational databases, so I can
join different tables together using primary/foreign keys.There's still an overwhelming amount of Flask content that I don't
know about, perhaps in the next project I can dive a bit deeeper!


I hope to keep the blog updated,so please check it again the
future! Thanks for your interest!

-bennyBoy

