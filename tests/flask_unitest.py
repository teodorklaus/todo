from run import app, URL
import unittest
import requests


class ErrorTests(unittest.TestCase):

#test app
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

#test url status
    def test_pagenotfound_statuscode(self):
        result = self.app.get(URL)

        self.assertEqual(result.status_code, 301)
        # print (self.assertEqual(result.status_code, 200))

#
    def test_pagenotfound_data(self):
        result = self.app.post(URL + 'add_todo/add')

        self.assertIn('404 Not Found', result.data)

    def test_status_code(self):
        headers = [('Accept-Encoding', 'gzip')]

        response = self.app.options('/', headers=headers)

        self.assertEqual(response.status_code, 200)
        # return (self.assertEqual(response.status_code, 404))

    def test_app_without_request(self):
        results = self.app.testing
        self.assertEquals(results, True)

    def request_code(self):
        # result_code = self.urllib.urlopen(URL).getcode()
        result_code = requests.get(URL)
        self.assertEqual(result_code, 111)



if __name__ == '__main__':
    unittest.main()