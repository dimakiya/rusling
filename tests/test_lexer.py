import unittest
from rusling.src.lexer import RuslingLexer

class TestRuslingLexer(unittest.TestCase):
    def test_variable_declaration(self):
        lexer = RuslingLexer()
        tokens = lexer.tokenize('перем x = /5\')
        # проверки токенов

if __name__ == '__main__':
    unittest.main()