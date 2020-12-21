from antlr4 import InputStream, CommonTokenStream

from day19 import match

from day19.part2.part2Lexer import part2Lexer
from day19.part2.part2Parser import part2Parser

if __name__ == '__main__':
    with open('input.txt') as data:
        total = 0
        for line in data.readlines():
            lexer = part2Lexer(InputStream(line))
            stream = CommonTokenStream(lexer)
            parser = part2Parser(stream)
            if match.matches(parser):
                total += 1

        print(total)