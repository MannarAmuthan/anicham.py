# Generated from grammar/Tamizh.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TamizhParser import TamizhParser
else:
    from TamizhParser import TamizhParser

# This class defines a complete listener for a parse tree produced by TamizhParser.
class TamizhListener(ParseTreeListener):

    # Enter a parse tree produced by TamizhParser#tamizh_script.
    def enterTamizh_script(self, ctx:TamizhParser.Tamizh_scriptContext):
        pass

    # Exit a parse tree produced by TamizhParser#tamizh_script.
    def exitTamizh_script(self, ctx:TamizhParser.Tamizh_scriptContext):
        pass


    # Enter a parse tree produced by TamizhParser#patthi.
    def enterPatthi(self, ctx:TamizhParser.PatthiContext):
        pass

    # Exit a parse tree produced by TamizhParser#patthi.
    def exitPatthi(self, ctx:TamizhParser.PatthiContext):
        pass


    # Enter a parse tree produced by TamizhParser#vaakiyam.
    def enterVaakiyam(self, ctx:TamizhParser.VaakiyamContext):
        pass

    # Exit a parse tree produced by TamizhParser#vaakiyam.
    def exitVaakiyam(self, ctx:TamizhParser.VaakiyamContext):
        pass


    # Enter a parse tree produced by TamizhParser#sol.
    def enterSol(self, ctx:TamizhParser.SolContext):
        pass

    # Exit a parse tree produced by TamizhParser#sol.
    def exitSol(self, ctx:TamizhParser.SolContext):
        pass


    # Enter a parse tree produced by TamizhParser#ezhuththu.
    def enterEzhuththu(self, ctx:TamizhParser.EzhuththuContext):
        pass

    # Exit a parse tree produced by TamizhParser#ezhuththu.
    def exitEzhuththu(self, ctx:TamizhParser.EzhuththuContext):
        pass



del TamizhParser