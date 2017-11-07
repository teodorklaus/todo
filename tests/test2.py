from app import *
import unittest




class ErrorTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_pagenotfound_statuscode(self):
        result = self.app.get('/add_todo')

        self.assertEqual(result.status_code, 404)
        print (result)


print (ErrorTests.test_pagenotfound_statuscode)