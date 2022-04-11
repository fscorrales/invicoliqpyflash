from flask import Flask

DATABASE = 'primary_key.sqlite'

app = Flask(__name__)
#http://localhost:5000/
@app.route('/')
def inicio():
    return 'Hola Mundo desde Flask'

#https://flask.palletsprojects.com/en/2.1.x/patterns/sqlite3/
# from flask import g
# import sqlite3

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv