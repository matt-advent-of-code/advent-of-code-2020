from antlr4 import Parser


def matches(parser: Parser) -> bool:
    try:
        parser.a0()
        return parser.getNumberOfSyntaxErrors() == 0
    except:
        return False
