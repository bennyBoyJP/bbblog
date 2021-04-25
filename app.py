from flask import Flask, render_template, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash
import database
from datestuff import date_stuff
from linkmaker import link_maker
from phrase_gen.word_gen1 import today_phrase


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
database.create_tables()
database.create_password_table()

# GLOBAL VARIABLES
# login global variable
access = False
# funny header phrase
phrase = today_phrase()


# ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def home():

    return render_template("index.html", entries=database.retrieve_entries(date_stuff("current")), phrase=phrase)


@app.route("/archives", methods=["GET", "POST"])
def archives():

    if request.method == "POST":
        data = request.form.get("dates_selected")

        date_selected = data.split()
        return render_template("retrieved.html", retrieved_entries=database.retrieved_entries(date_selected),
                               phrase=phrase)

    else:
        return render_template("archives.html", archives=database.pnt_archives(), phrase=phrase)


@app.route("/about", methods=["GET"])
def about():

    global phrase
    phrase = today_phrase()
    return render_template("about.html", phrase=phrase)


@app.route("/login", methods=["GET", "POST"])
def login():

    result = database.confirm_empty_pw_table()
    if not result:
        return redirect("/create_pw")

    if request.method == "POST":

        if database.confirm_empty_pw_table():
            attempt = request.form.get("password")
            pw = database.retrieve_password()

            match = check_password_hash(pw, attempt)

            if match:

                global access
                access = True

                return redirect("/admin")

            else:
                return render_template("login.html")
        else:
            return redirect("/create_pw")
    else:
        return render_template("login.html")


@app.route("/create_pw", methods=["GET", "POST"])
def create_pw():

    if request.method == "POST":
        pw = request.form.get("password")

        hashed_pw = generate_password_hash(pw)

        if not pw:
            return render_template("/create_pw.html")
        else:
            database.create_password(hashed_pw)
            return redirect("/login")

    return render_template("/create_pw.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if not access:
        return redirect("/login")

    else:
        if request.method == "POST":

            if request.form.get("title") == "delete all":
                database.del_entries()
                return render_template("admin.html", entries=database.retrieve_entries(date_stuff("current")),
                                       phrase=phrase)
            elif request.form.get("title") == "delete last":
                database.del_last_entry()
                return render_template("admin.html", entries=database.retrieve_entries(date_stuff("current")),
                                       phrase=phrase)

            if request.form.get("title"):
                entry_title = request.form.get("title")
            else:
                entry_title = "untitled"

            entry_content = request.form.get("content")
            entry_content_parts = link_maker(entry_content)

            if entry_content:
                database.create_entry(entry_title, entry_content_parts[0], date_stuff("timestamp"),
                                      entry_content_parts[1], entry_content_parts[2], date_stuff("log_month"),
                                      date_stuff("log_year"))

        return render_template("admin.html", entries=database.retrieve_entries(date_stuff("current")), phrase=phrase)
