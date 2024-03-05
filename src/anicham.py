from compiler import parse
from visitors.tamizh_visitor_impl import TamizhVisitorImpl


def from_string(string: str):
    tree = parse(string=string).tamizh_script()
    ast = TamizhVisitorImpl().visit(tree)
    return ast
