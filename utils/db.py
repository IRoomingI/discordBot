import sqlite3
from utils import paint, config
from sqlite3 import Error


# Setting up the database

database = "data.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_guild(sid, name, owner_id):
    conn = create_connection(database)
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO guilds(sid, name, owner_id, prefix) VALUES(?, ?, ?, ?)", (sid, name, owner_id, config.CONFIG["DEFAULT_PREFIX"]))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()


def delete_guild(sid):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("DELETE FROM guilds WHERE sid=?", (sid, ))
    c.execute("DELETE FROM colors WHERE sid=?", (sid, ))
    c.execute("DELETE FROM autoroles WHERE sid=?", (sid, ))
    conn.commit()
    conn.close()


# Color area

def create_color(sid, name, role_id):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO colors(uid, sid, name, role_id) VALUES(?, ?, ?, ?)",
              (sid + role_id, sid, name, role_id))
    conn.commit()
    conn.close()


def delete_color(sid, name, role_id):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("DELETE FROM colors WHERE sid=? AND name=? AND role_id=?",
              (sid, name, role_id))
    conn.commit()
    conn.close()


def fetch_colors(sid):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT name, role_id FROM colors WHERE sid=?", (sid, ))
    rows = c.fetchall()
    colors = {}
    for role in rows:
        colors[role[0]] = role[1]
    conn.close()
    return colors


# Autorole area

def create_autorole(sid, role_id):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO autoroles(uid, sid, role_id) VALUES(?, ?, ?)",
              (sid + role_id, sid, role_id))
    conn.commit()
    conn.close()


def delete_autorole(sid, role_id):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("DELETE FROM autoroles WHERE sid=? AND role_id=?", (sid, role_id))
    conn.commit()
    conn.close()


def fetch_autoroles(sid):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT role_id FROM autoroles WHERE sid=?", (sid, ))
    rows = c.fetchall()
    autoroles = []
    for r in rows:
        autoroles.append(r[0])
    conn.close()
    return autoroles


# Prefix area

def change_prefix(sid, prefix):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("UPDATE guilds SET prefix = ? WHERE sid=?",
              (prefix, sid))
    conn.commit()
    conn.close()


def fetch_prefix(sid):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT prefix FROM guilds WHERE sid=?", (sid, ))
    prefix = c.fetchone()[0]
    conn.close()
    return prefix


def fetchall_prefix():
    conn = create_connection(database)
    c = conn.cursor()
    c.execute("SELECT name, prefix FROM guilds")
    rows = c.fetchall()
    guild_prefix_dict = {}
    for r in rows:
        guild_prefix_dict[r[0]] = r[1]
    conn.close()
    return guild_prefix_dict


sql_create_guilds_table = """CREATE TABLE IF NOT EXISTS guilds (
                                sid int PRIMARY KEY,
                                name text NOT NULL,
                                owner_id int NOT NULL,
                                prefix text NOT NULL
); """

sql_create_colors_table = """CREATE TABLE IF NOT EXISTS colors (
                                uid text PRIMARY KEY,
                                sid int NOT NULL,
                                name text NOT NULL,
                                role_id int NOT NULL
);"""

sql_create_autoroles_table = """CREATE TABLE IF NOT EXISTS autoroles (
                                uid text PRIMARY KEY,
                                sid int NOT NULL,
                                role_id int NOT NULL
);"""

conn = create_connection(database)
if conn is not None:
    create_table(conn, sql_create_guilds_table)
    create_table(conn, sql_create_colors_table)
    create_table(conn, sql_create_autoroles_table)
else:
    print(paint.color("Cannot create database connection!", "red"))
    exit()

conn.close()
