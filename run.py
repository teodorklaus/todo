from app import *


#todo ajax query
#todo ajax request to server
#todo use SQLlite database
#todo travis CI
#todo Heroku


@app.route('/')# methods=['POST'])
def homepage():
    return render_template('index.html', messages=query_db('''select id, chacked, todo_text from todolist'''))


@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    ret_data_add = {"value": request.args.get('echoValue')}
    db = get_db()
    db.execute('''insert into todolist (chacked, todo_text)
                 values (?, ?)''', ('notchecked', ret_data_add['value']))
    db.commit()

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

#print (test())
if __name__ == '__main__':
    app.run()