import sqlite3


def run():
    select_table_names()


def select_table_names():
    for row in cur.execute("SELECT name FROM sqlite_master"):
        print(row)


if __name__ == "__main":
    con = sqlite3.connect("db.sqlite3", autocommit=False)
    cur = con.cursor()
    run()
    con.close()
