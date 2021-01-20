import unittest
import importlib

importlib.import_module("parser")

class TestParseMethods(unittest.TestCase):

    def test_opening_tag(self):
        token = parser.parse_opening_tag('<HTML>')
        self.assertEqual(str(token), 'HTML')
        self.assertTrue(token.isOpen())
    
    def test_closing_tag(self):
        token = parser.parse_closing_tag('</HTML>')
        self.assertEqual(str(token), 'HTML')
        self.assertFalse(token.isOpen())
    
    def test_inner_html(self):
        token = parser.parse_inner_html('Hello, world!')
        self.assertEqual(str(token))

    def test_parse_attribute(self):
        token = parser.parse_attributes('Key1=Value1 Key2=Value2  Key3=Value3')
        self.assertEqual(token.value['Key1'], 'Value1')
        self.assertEqual(token.value['Key2'], 'Value2')
        self.assertEqual(token.value['Key3'], 'Value3')
    