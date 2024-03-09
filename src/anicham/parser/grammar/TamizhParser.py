# Generated from grammar/Tamizh.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,4,1,19,8,1,11,1,12,1,20,1,1,1,1,1,2,4,2,
        26,8,2,11,2,12,2,27,1,2,1,2,1,2,1,3,4,3,34,8,3,11,3,12,3,35,1,3,
        5,3,39,8,3,10,3,12,3,42,9,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,
        48,49,2,0,1,14,27,41,45,0,11,1,0,0,0,2,18,1,0,0,0,4,25,1,0,0,0,6,
        33,1,0,0,0,8,43,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,
        0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,1,
        0,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,
        21,1,0,0,0,21,22,1,0,0,0,22,23,5,51,0,0,23,3,1,0,0,0,24,26,3,6,3,
        0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,
        1,0,0,0,29,30,5,50,0,0,30,31,5,49,0,0,31,5,1,0,0,0,32,34,3,8,4,0,
        33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,40,1,
        0,0,0,37,39,7,0,0,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,
        41,1,0,0,0,41,7,1,0,0,0,42,40,1,0,0,0,43,44,7,1,0,0,44,9,1,0,0,0,
        5,13,20,27,35,40
    ]

class TamizhParser ( Parser ):

    grammarFileName = "Tamizh.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\u0BCD'", 
                     "'\\u0BBE'", "'\\u0BBF'", "'\\u0BC0'", "'\\u0BC1'", 
                     "'\\u0BC2'", "'\\u0BC6'", "'\\u0BC7'", "'\\u0BC8'", 
                     "'\\u0BCA'", "'\\u0BCB'", "'\\u0BCC'", "'\\u0B83'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\u0B9C'", "'\\u0BB6'", 
                     "'\\u0BB7'", "'\\u0BB8'", "'\\u0BB9'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "MEI", "UYIR_MEI_OU", "UYIR_MEI_OA", 
                      "UYIR_MEI_O", "UYIR_MEI_AI", "UYIR_MEI_AE", "UYIR_MEI_E", 
                      "UYIR_MEI_OO", "UYIR_MEI_U", "UYIR_MEI_EE", "UYIR_MEI_I", 
                      "UYIR_MEI_AA", "UYIR_MEI_A", "UYIR", "PULLI", "KAAL", 
                      "SULI", "NEDIL_SULI", "U_KURIL", "U_NEDIL", "EA_KURIL", 
                      "EA_NEDIL", "I", "O_KURIL", "O_NEDIL", "OU", "AAYTHAM", 
                      "GRANTHA_SRI", "GRANTHA_MEI", "GRANTHA_OU", "GRANTHA_OA", 
                      "GRANTHA_O", "GRANTHA_AI", "GRANTHA_AE", "GRANTHA_E", 
                      "GRANTHA_OO", "GRANTHA_U", "GRANTHA_EE", "GRANTHA_I", 
                      "GRANTHA_AA", "GRANTHA_A", "GRANTHA_JA", "GRANTHA_SH", 
                      "GRANTHA_SS", "GRANTHA_S", "GRANTHA_H", "PUNCTUATIONS", 
                      "COMMA", "WS", "STOP_POINT", "NEWLINE" ]

    RULE_tamizh_script = 0
    RULE_patthi = 1
    RULE_vaakiyam = 2
    RULE_sol = 3
    RULE_ezhuththu = 4

    ruleNames =  [ "tamizh_script", "patthi", "vaakiyam", "sol", "ezhuththu" ]

    EOF = Token.EOF
    MEI=1
    UYIR_MEI_OU=2
    UYIR_MEI_OA=3
    UYIR_MEI_O=4
    UYIR_MEI_AI=5
    UYIR_MEI_AE=6
    UYIR_MEI_E=7
    UYIR_MEI_OO=8
    UYIR_MEI_U=9
    UYIR_MEI_EE=10
    UYIR_MEI_I=11
    UYIR_MEI_AA=12
    UYIR_MEI_A=13
    UYIR=14
    PULLI=15
    KAAL=16
    SULI=17
    NEDIL_SULI=18
    U_KURIL=19
    U_NEDIL=20
    EA_KURIL=21
    EA_NEDIL=22
    I=23
    O_KURIL=24
    O_NEDIL=25
    OU=26
    AAYTHAM=27
    GRANTHA_SRI=28
    GRANTHA_MEI=29
    GRANTHA_OU=30
    GRANTHA_OA=31
    GRANTHA_O=32
    GRANTHA_AI=33
    GRANTHA_AE=34
    GRANTHA_E=35
    GRANTHA_OO=36
    GRANTHA_U=37
    GRANTHA_EE=38
    GRANTHA_I=39
    GRANTHA_AA=40
    GRANTHA_A=41
    GRANTHA_JA=42
    GRANTHA_SH=43
    GRANTHA_SS=44
    GRANTHA_S=45
    GRANTHA_H=46
    PUNCTUATIONS=47
    COMMA=48
    WS=49
    STOP_POINT=50
    NEWLINE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Tamizh_scriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TamizhParser.EOF, 0)

        def patthi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TamizhParser.PatthiContext)
            else:
                return self.getTypedRuleContext(TamizhParser.PatthiContext,i)


        def getRuleIndex(self):
            return TamizhParser.RULE_tamizh_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTamizh_script" ):
                listener.enterTamizh_script(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTamizh_script" ):
                listener.exitTamizh_script(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTamizh_script" ):
                return visitor.visitTamizh_script(self)
            else:
                return visitor.visitChildren(self)




    def tamizh_script(self):

        localctx = TamizhParser.Tamizh_scriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tamizh_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.patthi()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4397912326142) != 0)):
                    break

            self.state = 15
            self.match(TamizhParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatthiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(TamizhParser.NEWLINE, 0)

        def vaakiyam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TamizhParser.VaakiyamContext)
            else:
                return self.getTypedRuleContext(TamizhParser.VaakiyamContext,i)


        def getRuleIndex(self):
            return TamizhParser.RULE_patthi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatthi" ):
                listener.enterPatthi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatthi" ):
                listener.exitPatthi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatthi" ):
                return visitor.visitPatthi(self)
            else:
                return visitor.visitChildren(self)




    def patthi(self):

        localctx = TamizhParser.PatthiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_patthi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.vaakiyam()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4397912326142) != 0)):
                    break

            self.state = 22
            self.match(TamizhParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VaakiyamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOP_POINT(self):
            return self.getToken(TamizhParser.STOP_POINT, 0)

        def WS(self):
            return self.getToken(TamizhParser.WS, 0)

        def sol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TamizhParser.SolContext)
            else:
                return self.getTypedRuleContext(TamizhParser.SolContext,i)


        def getRuleIndex(self):
            return TamizhParser.RULE_vaakiyam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVaakiyam" ):
                listener.enterVaakiyam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVaakiyam" ):
                listener.exitVaakiyam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVaakiyam" ):
                return visitor.visitVaakiyam(self)
            else:
                return visitor.visitChildren(self)




    def vaakiyam(self):

        localctx = TamizhParser.VaakiyamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vaakiyam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.sol()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4397912326142) != 0)):
                    break

            self.state = 29
            self.match(TamizhParser.STOP_POINT)
            self.state = 30
            self.match(TamizhParser.WS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ezhuththu(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TamizhParser.EzhuththuContext)
            else:
                return self.getTypedRuleContext(TamizhParser.EzhuththuContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TamizhParser.COMMA)
            else:
                return self.getToken(TamizhParser.COMMA, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TamizhParser.WS)
            else:
                return self.getToken(TamizhParser.WS, i)

        def getRuleIndex(self):
            return TamizhParser.RULE_sol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSol" ):
                listener.enterSol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSol" ):
                listener.exitSol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSol" ):
                return visitor.visitSol(self)
            else:
                return visitor.visitChildren(self)




    def sol(self):

        localctx = TamizhParser.SolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.ezhuththu()

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48 or _la==49:
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==48 or _la==49):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EzhuththuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UYIR(self):
            return self.getToken(TamizhParser.UYIR, 0)

        def MEI(self):
            return self.getToken(TamizhParser.MEI, 0)

        def AAYTHAM(self):
            return self.getToken(TamizhParser.AAYTHAM, 0)

        def UYIR_MEI_OU(self):
            return self.getToken(TamizhParser.UYIR_MEI_OU, 0)

        def UYIR_MEI_OA(self):
            return self.getToken(TamizhParser.UYIR_MEI_OA, 0)

        def UYIR_MEI_O(self):
            return self.getToken(TamizhParser.UYIR_MEI_O, 0)

        def UYIR_MEI_AI(self):
            return self.getToken(TamizhParser.UYIR_MEI_AI, 0)

        def UYIR_MEI_AE(self):
            return self.getToken(TamizhParser.UYIR_MEI_AE, 0)

        def UYIR_MEI_E(self):
            return self.getToken(TamizhParser.UYIR_MEI_E, 0)

        def UYIR_MEI_OO(self):
            return self.getToken(TamizhParser.UYIR_MEI_OO, 0)

        def UYIR_MEI_U(self):
            return self.getToken(TamizhParser.UYIR_MEI_U, 0)

        def UYIR_MEI_EE(self):
            return self.getToken(TamizhParser.UYIR_MEI_EE, 0)

        def UYIR_MEI_I(self):
            return self.getToken(TamizhParser.UYIR_MEI_I, 0)

        def UYIR_MEI_AA(self):
            return self.getToken(TamizhParser.UYIR_MEI_AA, 0)

        def UYIR_MEI_A(self):
            return self.getToken(TamizhParser.UYIR_MEI_A, 0)

        def GRANTHA_MEI(self):
            return self.getToken(TamizhParser.GRANTHA_MEI, 0)

        def GRANTHA_OU(self):
            return self.getToken(TamizhParser.GRANTHA_OU, 0)

        def GRANTHA_OA(self):
            return self.getToken(TamizhParser.GRANTHA_OA, 0)

        def GRANTHA_O(self):
            return self.getToken(TamizhParser.GRANTHA_O, 0)

        def GRANTHA_AI(self):
            return self.getToken(TamizhParser.GRANTHA_AI, 0)

        def GRANTHA_AE(self):
            return self.getToken(TamizhParser.GRANTHA_AE, 0)

        def GRANTHA_E(self):
            return self.getToken(TamizhParser.GRANTHA_E, 0)

        def GRANTHA_OO(self):
            return self.getToken(TamizhParser.GRANTHA_OO, 0)

        def GRANTHA_U(self):
            return self.getToken(TamizhParser.GRANTHA_U, 0)

        def GRANTHA_EE(self):
            return self.getToken(TamizhParser.GRANTHA_EE, 0)

        def GRANTHA_I(self):
            return self.getToken(TamizhParser.GRANTHA_I, 0)

        def GRANTHA_AA(self):
            return self.getToken(TamizhParser.GRANTHA_AA, 0)

        def GRANTHA_A(self):
            return self.getToken(TamizhParser.GRANTHA_A, 0)

        def GRANTHA_SRI(self):
            return self.getToken(TamizhParser.GRANTHA_SRI, 0)

        def getRuleIndex(self):
            return TamizhParser.RULE_ezhuththu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEzhuththu" ):
                listener.enterEzhuththu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEzhuththu" ):
                listener.exitEzhuththu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEzhuththu" ):
                return visitor.visitEzhuththu(self)
            else:
                return visitor.visitChildren(self)




    def ezhuththu(self):

        localctx = TamizhParser.EzhuththuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ezhuththu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4397912326142) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





