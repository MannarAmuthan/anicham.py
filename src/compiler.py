from antlr4 import InputStream, CommonTokenStream

from parser.grammar.TamizhLexer import TamizhLexer
from parser.grammar.TamizhParser import TamizhParser


def parse(
        file: str = None,
        string: str = None,
        turn_off_mismatch_error=True
):
    input_data = None
    if file:
        with open(file, 'r') as file:
            input_data = file.read()
    if string:
        input_data = string

    input_stream = InputStream(input_data)

    lexer = TamizhLexer(input_stream)
    if turn_off_mismatch_error:
        lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)
    parser = TamizhParser(stream)
    if turn_off_mismatch_error:
        parser.removeErrorListeners()
    return parser
