import unittest


from formatter.parser import Extractor
from formatter.parser import Parser
from formatter.directive import Directive


class TestMain(unittest.TestCase):

    def setUp(self):
        sql_path = './test.sql'
        format_path = './format.yaml'
        e = Extractor(sql_path,format_path)
        sql = e.sql_file
        format_ = e.format_file

        d = Directive(format_)
        d.data = sql
        w = d.create_with()
        # print(w)
        print(d.__repr__())


    def test_(self):
        self.assertTrue(False, True)
