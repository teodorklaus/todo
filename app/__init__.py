from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack, json
from sqlite3 import dbapi2 as sqlite3
import json
import sqlite3
from config import *


#DATABASE = (os.path.abspath("../todolist.db"))#'C:/Users/eduuser/Desktop/Python/todo/todolist.db'

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(__name__)
# app.config.from_envvar('MINITWIT_SETTINGS', silent=True)


def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect(DATABASE, check_same_thread = False)
con.row_factory = dict_factory #sqlite3.Row
cur = con.cursor()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
        #top.sqlite_db = sqlite3.connect(DATABASE, check_same_thread=False)
        #top.sqlite_db = sqlite3.connect()
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db


def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_database(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


@app.route('/')# methods=['POST'])
def homepage():
    return render_template('index.html', messages=query_db('''select id, chacked, todo_text from todolist'''))


@app.route('/add_todo', methods=['GET'])
def add_todo():
    ret_data_add = {"value": request.args.get('echoValue')}
    db = get_db()
    db.execute('''insert into todolist (chacked, todo_text)
                 values (?, ?)''', ('notchecked', ret_data_add['value']))
    db.commit()
    return ('add')


@app.route('/add_todo', methods=['POST'])
def add_todo1():
    cur.execute('''select id, chacked, todo_text from todolist where id = (select max(id) from todolist)''', ())
    rows = cur.fetchall()
    add_json = json.dumps(rows)
    return (add_json)


@app.route('/drop_todo', methods=['GET'])
def drop_todo():
    ret_data_drop = {"value": request.args.get('echoDelete')}
    ret_value = ret_data_drop['value']
    db = get_db()
    db.execute('delete from todolist where id=?', (ret_value,))
    db.commit()
    return ('Drop')

@app.route('/check_todo', methods=['GET'])
def check_todo():
    ret_data_checked = {"value": request.args.get('echoChecked')}
    ret_data_id = {"value": request.args.get('echoID')}
    ret_value_checked = ret_data_checked['value']
    ret_value_id = ret_data_id['value']
    db = get_db()
    db.execute('update todolist set chacked = ? where id = ?', (ret_value_checked, ret_value_id))
    db.commit()
    return ('Drop')
