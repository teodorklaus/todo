import os
import tempfile
import pytest
from app import *



@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    client = app.test_client()
    with app.app_context():
        init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


# def register(id = 150, chacked='nonchacked', todo_text='test'):
#     """Helper function to register a user"""
#     return client.post('/add_todo', data={ '0' : {
#         'id':     id,
#         'todo_text':     todo_text,
#         'chacked':    chacked,
#         }}, follow_redirects=True)


def add_message(client, text):
    """Records a message"""
    rv = client.post('/add_todo', data={'0' : {
        'id':     id,
        'todo_text':     'todo_text',
        'chacked':    'chacked',
        }},
                     follow_redirects=True)
    if text:
        assert b'Your message was recorded' in rv.data
    return rv

def test_message_recording(client):
    """Check if adding messages works"""
    add_message(client, 'test message 1')
    add_message(client, '<test message 2>')
    rv = client.get('/')
    assert b'test message 1' in rv.data
    assert b'&lt;test message 2&gt;' in rv.data
