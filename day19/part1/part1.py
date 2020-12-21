from antlr4 import InputStream, CommonTokenStream

from day19 import match
from day19.part1.part1Lexer import part1Lexer
from day19.part1.part1Parser import part1Parser

if __name__ == '__main__':
    with open('input.txt') as data:
        total = 0
        for line in data.readlines():
            lexer = part1Lexer(InputStream(line))
            stream = CommonTokenStream(lexer)
            parser = part1Parser(stream)
            if match.matches(parser):
                total += 1

        print(total)
