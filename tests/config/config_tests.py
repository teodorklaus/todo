import os

PORT = 8000
URL = 'http://127.0.0.1:' + str(PORT)



path_tofile = os.path.realpath(__file__)
path_dir = os.path.dirname(__file__)
path_tofile1 = os.path.abspath(os.path.join(path_dir, os.pardir))
path_to_todo = os.path.abspath(os.path.join(path_tofile1, os.pardir))


databasename = r'\todolist.db'

DATABASE_TEST = path_to_todo + databasename