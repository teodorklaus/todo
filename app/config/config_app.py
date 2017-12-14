import os


#DATABASE = (os.path.abspath("../../todolist.db"))#'../todo/todolist.db'

path_tofile = os.path.realpath(__file__)
path_dir = os.path.dirname(__file__)
path_tofile1 = os.path.abspath(os.path.join(path_dir, os.pardir))
path_to_todo = os.path.abspath(os.path.join(path_tofile1, os.pardir))


databasename = r'\todolist.db'

DATABASE = path_to_todo + databasename
PORT = 8000
URL = 'http://127.0.0.1:' + str(PORT)


# basedir = os.path.abspath(os.path.dirname(__file__))
#
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#
# print (SQLALCHEMY_DATABASE_URI)
# print (SQLALCHEMY_MIGRATE_REPO)
