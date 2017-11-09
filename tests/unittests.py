from run import *
#from app import config
import unittest


class ErrorTests(unittest.TestCase):

#test app
    def setUp(self):
        self.app = app.test_client()
        #self.client = app.test_client()
        self.app.testing = True

#test url status
    def test_pagenotfound_statuscode(self):
        result = self.app.get(url)

        self.assertEqual(result.status_code, 200)
        print (self.assertEqual(result.status_code, 200))

#
    def test_pagenotfound_data(self):
        result = self.app.post(url + 'add_todo/add')

        self.assertIn('404 Not Found', result.data)
        print(self.assertIn('404 Not Found', result.data))

    def test_status_code(self):
        headers = [('Accept-Encoding', 'gzip')]

        response = self.app.options('/', headers=headers)

        self.assertEqual(response.status_code, 200)
        return (self.assertEqual(response.status_code, 404))


