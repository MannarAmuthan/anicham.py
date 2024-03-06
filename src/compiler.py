from antlr4 import InputStream, CommonTokenStream

from parser.grammar.TamizhLexer import TamizhLexer
from parser.grammar.TamizhParser import TamizhParser


def parse(
        file_path: str = None,
        string: str = None,
        turn_off_mismatch_error=True
):
    input_data = None
    if file_path:
        with open(file_path, 'r') as file_path:
            input_data = file_path.read()
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
