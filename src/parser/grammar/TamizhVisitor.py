# Generated from grammar/Tamizh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TamizhParser import TamizhParser
else:
    from TamizhParser import TamizhParser

# This class defines a complete generic visitor for a parse tree produced by TamizhParser.

class TamizhVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TamizhParser#tamizh_script.
    def visitTamizh_script(self, ctx:TamizhParser.Tamizh_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamizhParser#patthi.
    def visitPatthi(self, ctx:TamizhParser.PatthiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamizhParser#vaakiyam.
    def visitVaakiyam(self, ctx:TamizhParser.VaakiyamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamizhParser#sol.
    def visitSol(self, ctx:TamizhParser.SolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamizhParser#ezhuththu.
    def visitEzhuththu(self, ctx:TamizhParser.EzhuththuContext):
        return self.visitChildren(ctx)



del TamizhParser