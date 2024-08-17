"""
C CREATE INSERT
R SELECT
U UPDATE
D DELETE DROP

Command Line Interface: python -m sqlite3 [-h] [-v] [filename] [sql]
"""

import sqlite3


def run():
    create_tables()
    select()


def create_tables():
    cur.execute(
        """ CREATE TABLE IF NOT EXISTS counters(
            category,
            count INTEGER)"""
    )
    cur.execute(
        """ CREATE TABLE IF NOT EXISTS players(
            first,
            last,
            email UNIQUE,
            active,
            verified,
            locked,
            created CURRENT_TIMESTAMP,
            UNIQUE(first, last))"""
    )
    cur.execute(
        """ CREATE TABLE IF NOT EXISTS verification(
        player_email,
        salt,
        hash,
        FOREIGN KEY(player_email) REFERENCES players(email))"""
    )


def select():
    for row in cur.execute("""SELECT name FROM sqlite_master"""):
        print(row)


if __name__ == "__main__":
    con = sqlite3.Connection(":memory:", autocommit=True)
    cur = con.cursor()
    run()
    con.close()
