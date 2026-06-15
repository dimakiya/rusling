import sys
import os
from .lexer import RuslingLexer
from .parser import RuslingParser

class RuslingInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        lexer = RuslingLexer()
        tokens = lexer.tokenize(code)

        parser = RuslingParser()
        ast = parser.parse(tokens)

        self._execute_ast(ast)

    def _execute_ast(self, ast):
        # логика выполнения AST
        pass

def main():
    if len(sys.argv) != 2:
        print("Использование: rusling <файл.rusl>")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.lower().endswith('.rusl'):
        print(f"Ошибка: файл должен иметь расширение .rusl")
        sys.exit(1)

    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        sys.exit(1)

    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.read()

    interpreter = RuslingInterpreter()
    interpreter.execute(source_code)
