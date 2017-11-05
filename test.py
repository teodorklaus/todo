from app import *

con = sqlite3.connect(DATABASE)
cur = con.cursor()
curs = query_db('''select todo_text from todolist LIMIT 1''')


print curs


if __name__ == '__main__':
    app.run()