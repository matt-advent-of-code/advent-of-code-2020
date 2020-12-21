import unittest

from antlr4 import InputStream, CommonTokenStream

from day19 import match
from day19.simple.simpleLexer import simpleLexer
from day19.simple.simpleParser import simpleParser

class MyTestCase(unittest.TestCase):
    def test_pass(self):
        lexer = simpleLexer(InputStream('aab'))
        stream = CommonTokenStream(lexer)
        parser = simpleParser(stream)

        self.assertTrue(match.matches(parser))

    def test_fail(self):
        lexer = simpleLexer(InputStream('abb'))
        stream = CommonTokenStream(lexer)
        parser = simpleParser(stream)

        self.assertFalse(match.matches(parser))


if __name__ == '__main__':
    unittest.main()
