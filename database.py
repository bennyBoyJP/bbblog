import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries " \
               "(title TEXT, content TEXT, date TEXT, link TEXT, link_name TEXT, month TEXT, year TEXT)"
CREATE_ENTRY = "INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?)"
RETRIEVE_ENTRIES = "SELECT * FROM entries WHERE month = (?) AND year = (?) ORDER BY rowid DESC"
DELETE_ENTRIES = "DELETE FROM entries"
DELETE_LAST_ENTRY = "DELETE FROM entries WHERE rowid = (SELECT MAX(rowid) FROM entries)"
PRINT_ARCHIVES = "SELECT DISTINCT month, year FROM entries"
SEARCH_QUERY = "SELECT * FROM entries WHERE month = (?) AND year = (?)"
CREATE_PASSWORD_TABLE = "CREATE TABLE IF NOT EXISTS account (hash_pw TEXT)"
CONFIRM_EMPTY_PW_TABLE = "SELECT COUNT(*) FROM account"
CREATE_PASSWORD = "INSERT INTO account VALUES (?)"
RETRIEVE_PASSWORD = "SELECT * FROM account"


def create_tables():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE)


def create_entry(title, content, date, link, link_name, month, year):

    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_ENTRY, (title, content, date, link, link_name, month, year))


def retrieve_entries(query):

    cm = query[0]  # current month
    cy = query[-1]  # current year

    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES, (cm, cy))
        return cursor.fetchall()


def del_entries():

    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ENTRIES)


def del_last_entry():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_LAST_ENTRY)

def pnt_archives():

    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        # cursor.execute(PRINT_ARCHIVES)
        return cursor.execute(PRINT_ARCHIVES)


def retrieved_entries(query):

    with sqlite3.connect("data.db") as connection:

        m = query[0]  # month
        y = query[-1]  # year

        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES, (m, y))

        return cursor.fetchall()


def create_password_table():

    with sqlite3.connect("pw_table.db") as connection:
        connection.execute(CREATE_PASSWORD_TABLE)


def confirm_empty_pw_table():

    with sqlite3.connect("pw_table.db") as connection:
        cursor = connection.cursor()
        cursor.execute(CONFIRM_EMPTY_PW_TABLE)
        return int(cursor.fetchone()[0])


def create_password(pw):

    with sqlite3.connect("pw_table.db") as connection:
        connection.execute(CREATE_PASSWORD, (pw,))


def retrieve_password():

    with sqlite3.connect("pw_table.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_PASSWORD)
        return cursor.fetchone()[0]

