import datetime


def date_stuff(query):
    def number_day_suffix(n):
        if n[-1] == "1" and n != "11":
            return f"{n}st"
        if n[-1] == "2" and n != "12":
            return f"{n}nd"
        if n[-1] == "3" and n != "13":
            return f"{n}rd"
        else:
            return f"{n}th"

    day_suffix = number_day_suffix(datetime.datetime.today().strftime("%d"))
    entry_date = "{0}{1}{2}".format(datetime.datetime.today().strftime("%A, %B "),
                                    str(day_suffix),
                                    datetime.datetime.today().strftime(", %Y at %H:%M"))
    entry_month = "{0}".format(datetime.datetime.today().strftime("%m"))
    entry_year = "{0}".format(datetime.datetime.today().strftime("%Y"))
    current_date = [entry_month, entry_year]

    if query == "current":
        return current_date
    elif query == "timestamp":
        return entry_date
    elif query == "log_month":
        return entry_month
    elif query == "log_year":
        return entry_year
