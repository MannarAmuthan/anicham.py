from parser.grammar.TamizhLexer import TamizhLexer
from parser.grammar.TamizhVisitor import TamizhVisitor
from parser.grammar.TamizhParser import TamizhParser
from antlr4 import *

from visitors.tamizh_visitor_impl import TamizhVisitorImpl


def main():
    with open('/Users/amuthanm/Documents/personal/anicham.py/sample.txt', 'r') as file:
        input_data = file.read()

    input_stream = InputStream(input_data)

    lexer = TamizhLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TamizhParser(stream)
    tree = parser.patthi()
    ast = TamizhVisitorImpl().visit(tree)


if __name__ == '__main__':
    main()
