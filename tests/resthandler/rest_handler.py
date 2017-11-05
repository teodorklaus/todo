import unittest

import tornado.web
import python_rest_handler
from tornado_rest_handler import *

class Model(object):
    pass

class TemplatePathTests(unittest.TestCase):
    def test_rest_routes(self):
        cls = rest_routes(Model)[0][1]
        self.assertEqual(True, issubclass(cls, TornadoRestHandler))
        self.assertEquals(True, issubclass(cls, tornado.web.RequestHandler))
        self.assertEquals(True, issubclass(cls, python_rest_handler.RestRequestHandler))

        self.assertEquals(MongoEngineDataManager, cls.data_manager)

        #self.assertEquals('index.html', cls.index_template)
        self.assertEquals('/', cls.redirect_pos_action)