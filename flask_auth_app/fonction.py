
import sqlite3
from flask import current_app , g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    #app.cli.add_command(init_db_command)

def get_familles():
    database = sqlite3.connect('test.db')
    cursor = database.cursor()
    famille=[]
    cursor.execute("SELECT NOM from FAMILLES")
    famille_tempo = cursor.fetchall()
    famille_tempo = [i[0] for i in famille_tempo]
    return famille_tempo

def get_date():
    database = sqlite3.connect('test.db')
    cursor = database.cursor()
    cursor.execute("SELECT DATE from VELAGES")
    dates_tempo = []
    for i in cursor:
        dates_tempo.append(i[0])
        
    return dates_tempo


