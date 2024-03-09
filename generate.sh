pip3 install antlr4-tools

antlr4 -Dlanguage=Python3 grammar/Tamizh.g4 -o src/parser/ -visitor
antlr4 -Dlanguage=Python3 grammar/Yappu/Venba.g4 -o src/parser/ -visitor