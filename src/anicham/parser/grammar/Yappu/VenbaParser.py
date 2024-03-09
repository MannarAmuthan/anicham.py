# Generated from grammar/Yappu/Venba.g4 by ANTLR 4.13.1
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
        4,1,40,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,4,0,52,8,0,11,0,12,
        0,53,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,84,8,
        4,1,5,1,5,1,5,1,5,3,5,90,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,
        1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,
        13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,
        17,1,18,1,18,1,18,1,18,3,18,132,8,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,4,19,143,8,19,11,19,12,19,144,1,19,1,19,1,19,4,
        19,150,8,19,11,19,12,19,151,3,19,154,8,19,1,20,1,20,1,20,4,20,159,
        8,20,11,20,12,20,160,1,20,1,20,1,20,4,20,166,8,20,11,20,12,20,167,
        3,20,170,8,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,0,0,24,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,3,9,
        0,4,4,7,7,9,9,11,11,13,14,16,16,18,18,20,20,23,23,10,0,2,3,5,6,8,
        8,10,10,12,12,15,15,17,17,19,19,21,22,24,25,2,0,1,1,26,26,178,0,
        51,1,0,0,0,2,57,1,0,0,0,4,65,1,0,0,0,6,73,1,0,0,0,8,83,1,0,0,0,10,
        89,1,0,0,0,12,91,1,0,0,0,14,94,1,0,0,0,16,97,1,0,0,0,18,100,1,0,
        0,0,20,103,1,0,0,0,22,106,1,0,0,0,24,109,1,0,0,0,26,112,1,0,0,0,
        28,115,1,0,0,0,30,118,1,0,0,0,32,121,1,0,0,0,34,124,1,0,0,0,36,131,
        1,0,0,0,38,153,1,0,0,0,40,169,1,0,0,0,42,171,1,0,0,0,44,173,1,0,
        0,0,46,175,1,0,0,0,48,49,3,2,1,0,49,50,5,39,0,0,50,52,1,0,0,0,51,
        48,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,
        0,55,56,3,4,2,0,56,1,1,0,0,0,57,58,3,6,3,0,58,59,5,40,0,0,59,60,
        3,6,3,0,60,61,5,40,0,0,61,62,3,6,3,0,62,63,5,40,0,0,63,64,3,6,3,
        0,64,3,1,0,0,0,65,66,3,6,3,0,66,67,5,40,0,0,67,68,3,6,3,0,68,69,
        5,40,0,0,69,70,3,36,18,0,70,5,1,0,0,0,71,74,3,10,5,0,72,74,3,8,4,
        0,73,71,1,0,0,0,73,72,1,0,0,0,74,7,1,0,0,0,75,84,3,12,6,0,76,84,
        3,16,8,0,77,84,3,20,10,0,78,84,3,24,12,0,79,84,3,14,7,0,80,84,3,
        18,9,0,81,84,3,22,11,0,82,84,3,26,13,0,83,75,1,0,0,0,83,76,1,0,0,
        0,83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,
        1,0,0,0,83,82,1,0,0,0,84,9,1,0,0,0,85,90,3,34,17,0,86,90,3,30,15,
        0,87,90,3,32,16,0,88,90,3,28,14,0,89,85,1,0,0,0,89,86,1,0,0,0,89,
        87,1,0,0,0,89,88,1,0,0,0,90,11,1,0,0,0,91,92,3,28,14,0,92,93,3,40,
        20,0,93,13,1,0,0,0,94,95,3,28,14,0,95,96,3,38,19,0,96,15,1,0,0,0,
        97,98,3,30,15,0,98,99,3,40,20,0,99,17,1,0,0,0,100,101,3,30,15,0,
        101,102,3,38,19,0,102,19,1,0,0,0,103,104,3,32,16,0,104,105,3,40,
        20,0,105,21,1,0,0,0,106,107,3,32,16,0,107,108,3,38,19,0,108,23,1,
        0,0,0,109,110,3,34,17,0,110,111,3,40,20,0,111,25,1,0,0,0,112,113,
        3,34,17,0,113,114,3,38,19,0,114,27,1,0,0,0,115,116,3,40,20,0,116,
        117,3,40,20,0,117,29,1,0,0,0,118,119,3,38,19,0,119,120,3,40,20,0,
        120,31,1,0,0,0,121,122,3,40,20,0,122,123,3,38,19,0,123,33,1,0,0,
        0,124,125,3,38,19,0,125,126,3,38,19,0,126,35,1,0,0,0,127,132,3,40,
        20,0,128,132,3,38,19,0,129,132,3,28,14,0,130,132,3,30,15,0,131,127,
        1,0,0,0,131,128,1,0,0,0,131,129,1,0,0,0,131,130,1,0,0,0,132,37,1,
        0,0,0,133,134,3,42,21,0,134,135,3,42,21,0,135,154,1,0,0,0,136,137,
        3,42,21,0,137,138,3,44,22,0,138,154,1,0,0,0,139,140,3,42,21,0,140,
        142,3,42,21,0,141,143,3,46,23,0,142,141,1,0,0,0,143,144,1,0,0,0,
        144,142,1,0,0,0,144,145,1,0,0,0,145,154,1,0,0,0,146,147,3,42,21,
        0,147,149,3,44,22,0,148,150,3,46,23,0,149,148,1,0,0,0,150,151,1,
        0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,133,1,
        0,0,0,153,136,1,0,0,0,153,139,1,0,0,0,153,146,1,0,0,0,154,39,1,0,
        0,0,155,170,3,42,21,0,156,158,3,42,21,0,157,159,3,46,23,0,158,157,
        1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,170,
        1,0,0,0,162,170,3,44,22,0,163,165,3,44,22,0,164,166,3,46,23,0,165,
        164,1,0,0,0,166,167,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        170,1,0,0,0,169,155,1,0,0,0,169,156,1,0,0,0,169,162,1,0,0,0,169,
        163,1,0,0,0,170,41,1,0,0,0,171,172,7,0,0,0,172,43,1,0,0,0,173,174,
        7,1,0,0,174,45,1,0,0,0,175,176,7,2,0,0,176,47,1,0,0,0,11,53,73,83,
        89,131,144,151,153,160,167,169
    ]

class VenbaParser ( Parser ):

    grammarFileName = "Venba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\u0B85'", "'\\u0B86'", 
                     "'\\u0B87'", "'\\u0B88'", "'\\u0B89'", "'\\u0B8A'", 
                     "'\\u0B8E'", "'\\u0B8F'", "'\\u0B90'", "'\\u0B92'", 
                     "'\\u0B93'", "'\\u0B94'", "'\\u0B83'", "'\\u0BCD'", 
                     "'\\u0BBE'", "'\\u0BBF'", "'\\u0BC0'", "'\\u0BC1'", 
                     "'\\u0BC2'", "'\\u0BC6'", "'\\u0BC7'", "'\\u0BC8'", 
                     "'\\u0BCA'", "'\\u0BCB'", "'\\u0BCC'" ]

    symbolicNames = [ "<INVALID>", "MEI", "UYIR_MEI_OU", "UYIR_MEI_OA", 
                      "UYIR_MEI_O", "UYIR_MEI_AI", "UYIR_MEI_AE", "UYIR_MEI_E", 
                      "UYIR_MEI_OO", "UYIR_MEI_U", "UYIR_MEI_EE", "UYIR_MEI_I", 
                      "UYIR_MEI_AA", "UYIR_MEI_A", "A_UYIR", "AA_UYIR", 
                      "I_UYIR", "EE_UYIR", "U_UYIR", "OO_UYIR", "E_UYIR", 
                      "AE_UYIR", "AI_UYIR", "O_UYIR", "OA_UYIR", "OU_UYIR", 
                      "AAYTHAM", "PULLI", "KAAL", "SULI", "NEDIL_SULI", 
                      "U_KURIL", "U_NEDIL", "EA_KURIL", "EA_NEDIL", "I", 
                      "O_KURIL", "O_NEDIL", "OU", "NEWLINE", "WS" ]

    RULE_venba = 0
    RULE_adi = 1
    RULE_eetradi = 2
    RULE_seer = 3
    RULE_moovasai = 4
    RULE_eerasai = 5
    RULE_themangai = 6
    RULE_themangani = 7
    RULE_pulimangai = 8
    RULE_pulimangani = 9
    RULE_koovilangai = 10
    RULE_koovilangani = 11
    RULE_karuvilangai = 12
    RULE_karuvilangani = 13
    RULE_thema = 14
    RULE_pulima = 15
    RULE_koovilam = 16
    RULE_karuvilam = 17
    RULE_eetru_seer = 18
    RULE_nirai_asai = 19
    RULE_ner_asai = 20
    RULE_kuril = 21
    RULE_nedil = 22
    RULE_otru = 23

    ruleNames =  [ "venba", "adi", "eetradi", "seer", "moovasai", "eerasai", 
                   "themangai", "themangani", "pulimangai", "pulimangani", 
                   "koovilangai", "koovilangani", "karuvilangai", "karuvilangani", 
                   "thema", "pulima", "koovilam", "karuvilam", "eetru_seer", 
                   "nirai_asai", "ner_asai", "kuril", "nedil", "otru" ]

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
    A_UYIR=14
    AA_UYIR=15
    I_UYIR=16
    EE_UYIR=17
    U_UYIR=18
    OO_UYIR=19
    E_UYIR=20
    AE_UYIR=21
    AI_UYIR=22
    O_UYIR=23
    OA_UYIR=24
    OU_UYIR=25
    AAYTHAM=26
    PULLI=27
    KAAL=28
    SULI=29
    NEDIL_SULI=30
    U_KURIL=31
    U_NEDIL=32
    EA_KURIL=33
    EA_NEDIL=34
    I=35
    O_KURIL=36
    O_NEDIL=37
    OU=38
    NEWLINE=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class VenbaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eetradi(self):
            return self.getTypedRuleContext(VenbaParser.EetradiContext,0)


        def adi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.AdiContext)
            else:
                return self.getTypedRuleContext(VenbaParser.AdiContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(VenbaParser.NEWLINE)
            else:
                return self.getToken(VenbaParser.NEWLINE, i)

        def getRuleIndex(self):
            return VenbaParser.RULE_venba

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVenba" ):
                listener.enterVenba(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVenba" ):
                listener.exitVenba(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVenba" ):
                return visitor.visitVenba(self)
            else:
                return visitor.visitChildren(self)




    def venba(self):

        localctx = VenbaParser.VenbaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_venba)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 48
                    self.adi()
                    self.state = 49
                    self.match(VenbaParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 53 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 55
            self.eetradi()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.SeerContext)
            else:
                return self.getTypedRuleContext(VenbaParser.SeerContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(VenbaParser.WS)
            else:
                return self.getToken(VenbaParser.WS, i)

        def getRuleIndex(self):
            return VenbaParser.RULE_adi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdi" ):
                listener.enterAdi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdi" ):
                listener.exitAdi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdi" ):
                return visitor.visitAdi(self)
            else:
                return visitor.visitChildren(self)




    def adi(self):

        localctx = VenbaParser.AdiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_adi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.seer()
            self.state = 58
            self.match(VenbaParser.WS)
            self.state = 59
            self.seer()
            self.state = 60
            self.match(VenbaParser.WS)
            self.state = 61
            self.seer()
            self.state = 62
            self.match(VenbaParser.WS)
            self.state = 63
            self.seer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EetradiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.SeerContext)
            else:
                return self.getTypedRuleContext(VenbaParser.SeerContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(VenbaParser.WS)
            else:
                return self.getToken(VenbaParser.WS, i)

        def eetru_seer(self):
            return self.getTypedRuleContext(VenbaParser.Eetru_seerContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_eetradi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEetradi" ):
                listener.enterEetradi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEetradi" ):
                listener.exitEetradi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEetradi" ):
                return visitor.visitEetradi(self)
            else:
                return visitor.visitChildren(self)




    def eetradi(self):

        localctx = VenbaParser.EetradiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_eetradi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.seer()
            self.state = 66
            self.match(VenbaParser.WS)
            self.state = 67
            self.seer()
            self.state = 68
            self.match(VenbaParser.WS)
            self.state = 69
            self.eetru_seer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eerasai(self):
            return self.getTypedRuleContext(VenbaParser.EerasaiContext,0)


        def moovasai(self):
            return self.getTypedRuleContext(VenbaParser.MoovasaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_seer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeer" ):
                listener.enterSeer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeer" ):
                listener.exitSeer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeer" ):
                return visitor.visitSeer(self)
            else:
                return visitor.visitChildren(self)




    def seer(self):

        localctx = VenbaParser.SeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_seer)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.eerasai()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.moovasai()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoovasaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def themangai(self):
            return self.getTypedRuleContext(VenbaParser.ThemangaiContext,0)


        def pulimangai(self):
            return self.getTypedRuleContext(VenbaParser.PulimangaiContext,0)


        def koovilangai(self):
            return self.getTypedRuleContext(VenbaParser.KoovilangaiContext,0)


        def karuvilangai(self):
            return self.getTypedRuleContext(VenbaParser.KaruvilangaiContext,0)


        def themangani(self):
            return self.getTypedRuleContext(VenbaParser.ThemanganiContext,0)


        def pulimangani(self):
            return self.getTypedRuleContext(VenbaParser.PulimanganiContext,0)


        def koovilangani(self):
            return self.getTypedRuleContext(VenbaParser.KoovilanganiContext,0)


        def karuvilangani(self):
            return self.getTypedRuleContext(VenbaParser.KaruvilanganiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_moovasai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoovasai" ):
                listener.enterMoovasai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoovasai" ):
                listener.exitMoovasai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoovasai" ):
                return visitor.visitMoovasai(self)
            else:
                return visitor.visitChildren(self)




    def moovasai(self):

        localctx = VenbaParser.MoovasaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_moovasai)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.themangai()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.pulimangai()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.koovilangai()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.karuvilangai()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.themangani()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.pulimangani()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.koovilangani()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.karuvilangani()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EerasaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def karuvilam(self):
            return self.getTypedRuleContext(VenbaParser.KaruvilamContext,0)


        def pulima(self):
            return self.getTypedRuleContext(VenbaParser.PulimaContext,0)


        def koovilam(self):
            return self.getTypedRuleContext(VenbaParser.KoovilamContext,0)


        def thema(self):
            return self.getTypedRuleContext(VenbaParser.ThemaContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_eerasai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEerasai" ):
                listener.enterEerasai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEerasai" ):
                listener.exitEerasai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEerasai" ):
                return visitor.visitEerasai(self)
            else:
                return visitor.visitChildren(self)




    def eerasai(self):

        localctx = VenbaParser.EerasaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_eerasai)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.karuvilam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.pulima()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.koovilam()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.thema()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThemangaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def thema(self):
            return self.getTypedRuleContext(VenbaParser.ThemaContext,0)


        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_themangai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThemangai" ):
                listener.enterThemangai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThemangai" ):
                listener.exitThemangai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThemangai" ):
                return visitor.visitThemangai(self)
            else:
                return visitor.visitChildren(self)




    def themangai(self):

        localctx = VenbaParser.ThemangaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_themangai)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.thema()
            self.state = 92
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThemanganiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def thema(self):
            return self.getTypedRuleContext(VenbaParser.ThemaContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_themangani

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThemangani" ):
                listener.enterThemangani(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThemangani" ):
                listener.exitThemangani(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThemangani" ):
                return visitor.visitThemangani(self)
            else:
                return visitor.visitChildren(self)




    def themangani(self):

        localctx = VenbaParser.ThemanganiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_themangani)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.thema()
            self.state = 95
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PulimangaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pulima(self):
            return self.getTypedRuleContext(VenbaParser.PulimaContext,0)


        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_pulimangai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPulimangai" ):
                listener.enterPulimangai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPulimangai" ):
                listener.exitPulimangai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPulimangai" ):
                return visitor.visitPulimangai(self)
            else:
                return visitor.visitChildren(self)




    def pulimangai(self):

        localctx = VenbaParser.PulimangaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pulimangai)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.pulima()
            self.state = 98
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PulimanganiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pulima(self):
            return self.getTypedRuleContext(VenbaParser.PulimaContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_pulimangani

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPulimangani" ):
                listener.enterPulimangani(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPulimangani" ):
                listener.exitPulimangani(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPulimangani" ):
                return visitor.visitPulimangani(self)
            else:
                return visitor.visitChildren(self)




    def pulimangani(self):

        localctx = VenbaParser.PulimanganiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pulimangani)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.pulima()
            self.state = 101
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KoovilangaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def koovilam(self):
            return self.getTypedRuleContext(VenbaParser.KoovilamContext,0)


        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_koovilangai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKoovilangai" ):
                listener.enterKoovilangai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKoovilangai" ):
                listener.exitKoovilangai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKoovilangai" ):
                return visitor.visitKoovilangai(self)
            else:
                return visitor.visitChildren(self)




    def koovilangai(self):

        localctx = VenbaParser.KoovilangaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_koovilangai)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.koovilam()
            self.state = 104
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KoovilanganiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def koovilam(self):
            return self.getTypedRuleContext(VenbaParser.KoovilamContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_koovilangani

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKoovilangani" ):
                listener.enterKoovilangani(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKoovilangani" ):
                listener.exitKoovilangani(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKoovilangani" ):
                return visitor.visitKoovilangani(self)
            else:
                return visitor.visitChildren(self)




    def koovilangani(self):

        localctx = VenbaParser.KoovilanganiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_koovilangani)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.koovilam()
            self.state = 107
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KaruvilangaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def karuvilam(self):
            return self.getTypedRuleContext(VenbaParser.KaruvilamContext,0)


        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_karuvilangai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKaruvilangai" ):
                listener.enterKaruvilangai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKaruvilangai" ):
                listener.exitKaruvilangai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKaruvilangai" ):
                return visitor.visitKaruvilangai(self)
            else:
                return visitor.visitChildren(self)




    def karuvilangai(self):

        localctx = VenbaParser.KaruvilangaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_karuvilangai)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.karuvilam()
            self.state = 110
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KaruvilanganiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def karuvilam(self):
            return self.getTypedRuleContext(VenbaParser.KaruvilamContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_karuvilangani

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKaruvilangani" ):
                listener.enterKaruvilangani(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKaruvilangani" ):
                listener.exitKaruvilangani(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKaruvilangani" ):
                return visitor.visitKaruvilangani(self)
            else:
                return visitor.visitChildren(self)




    def karuvilangani(self):

        localctx = VenbaParser.KaruvilanganiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_karuvilangani)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.karuvilam()
            self.state = 113
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ner_asai(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.Ner_asaiContext)
            else:
                return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,i)


        def getRuleIndex(self):
            return VenbaParser.RULE_thema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThema" ):
                listener.enterThema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThema" ):
                listener.exitThema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThema" ):
                return visitor.visitThema(self)
            else:
                return visitor.visitChildren(self)




    def thema(self):

        localctx = VenbaParser.ThemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_thema)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.ner_asai()
            self.state = 116
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PulimaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_pulima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPulima" ):
                listener.enterPulima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPulima" ):
                listener.exitPulima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPulima" ):
                return visitor.visitPulima(self)
            else:
                return visitor.visitChildren(self)




    def pulima(self):

        localctx = VenbaParser.PulimaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pulima)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.nirai_asai()
            self.state = 119
            self.ner_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KoovilamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_koovilam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKoovilam" ):
                listener.enterKoovilam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKoovilam" ):
                listener.exitKoovilam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKoovilam" ):
                return visitor.visitKoovilam(self)
            else:
                return visitor.visitChildren(self)




    def koovilam(self):

        localctx = VenbaParser.KoovilamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_koovilam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.ner_asai()
            self.state = 122
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KaruvilamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nirai_asai(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.Nirai_asaiContext)
            else:
                return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,i)


        def getRuleIndex(self):
            return VenbaParser.RULE_karuvilam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKaruvilam" ):
                listener.enterKaruvilam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKaruvilam" ):
                listener.exitKaruvilam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKaruvilam" ):
                return visitor.visitKaruvilam(self)
            else:
                return visitor.visitChildren(self)




    def karuvilam(self):

        localctx = VenbaParser.KaruvilamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_karuvilam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.nirai_asai()
            self.state = 125
            self.nirai_asai()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eetru_seerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ner_asai(self):
            return self.getTypedRuleContext(VenbaParser.Ner_asaiContext,0)


        def nirai_asai(self):
            return self.getTypedRuleContext(VenbaParser.Nirai_asaiContext,0)


        def thema(self):
            return self.getTypedRuleContext(VenbaParser.ThemaContext,0)


        def pulima(self):
            return self.getTypedRuleContext(VenbaParser.PulimaContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_eetru_seer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEetru_seer" ):
                listener.enterEetru_seer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEetru_seer" ):
                listener.exitEetru_seer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEetru_seer" ):
                return visitor.visitEetru_seer(self)
            else:
                return visitor.visitChildren(self)




    def eetru_seer(self):

        localctx = VenbaParser.Eetru_seerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_eetru_seer)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.ner_asai()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.nirai_asai()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.thema()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.pulima()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nirai_asaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kuril(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.KurilContext)
            else:
                return self.getTypedRuleContext(VenbaParser.KurilContext,i)


        def nedil(self):
            return self.getTypedRuleContext(VenbaParser.NedilContext,0)


        def otru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.OtruContext)
            else:
                return self.getTypedRuleContext(VenbaParser.OtruContext,i)


        def getRuleIndex(self):
            return VenbaParser.RULE_nirai_asai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNirai_asai" ):
                listener.enterNirai_asai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNirai_asai" ):
                listener.exitNirai_asai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNirai_asai" ):
                return visitor.visitNirai_asai(self)
            else:
                return visitor.visitChildren(self)




    def nirai_asai(self):

        localctx = VenbaParser.Nirai_asaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_nirai_asai)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.kuril()
                self.state = 134
                self.kuril()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.kuril()
                self.state = 137
                self.nedil()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.kuril()
                self.state = 140
                self.kuril()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 141
                    self.otru()
                    self.state = 144 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==26):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.kuril()
                self.state = 147
                self.nedil()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 148
                    self.otru()
                    self.state = 151 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==26):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ner_asaiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kuril(self):
            return self.getTypedRuleContext(VenbaParser.KurilContext,0)


        def otru(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VenbaParser.OtruContext)
            else:
                return self.getTypedRuleContext(VenbaParser.OtruContext,i)


        def nedil(self):
            return self.getTypedRuleContext(VenbaParser.NedilContext,0)


        def getRuleIndex(self):
            return VenbaParser.RULE_ner_asai

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNer_asai" ):
                listener.enterNer_asai(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNer_asai" ):
                listener.exitNer_asai(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNer_asai" ):
                return visitor.visitNer_asai(self)
            else:
                return visitor.visitChildren(self)




    def ner_asai(self):

        localctx = VenbaParser.Ner_asaiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ner_asai)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.kuril()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.kuril()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 157
                    self.otru()
                    self.state = 160 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==26):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.nedil()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.nedil()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 164
                    self.otru()
                    self.state = 167 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==26):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KurilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A_UYIR(self):
            return self.getToken(VenbaParser.A_UYIR, 0)

        def I_UYIR(self):
            return self.getToken(VenbaParser.I_UYIR, 0)

        def U_UYIR(self):
            return self.getToken(VenbaParser.U_UYIR, 0)

        def E_UYIR(self):
            return self.getToken(VenbaParser.E_UYIR, 0)

        def O_UYIR(self):
            return self.getToken(VenbaParser.O_UYIR, 0)

        def UYIR_MEI_A(self):
            return self.getToken(VenbaParser.UYIR_MEI_A, 0)

        def UYIR_MEI_I(self):
            return self.getToken(VenbaParser.UYIR_MEI_I, 0)

        def UYIR_MEI_U(self):
            return self.getToken(VenbaParser.UYIR_MEI_U, 0)

        def UYIR_MEI_E(self):
            return self.getToken(VenbaParser.UYIR_MEI_E, 0)

        def UYIR_MEI_O(self):
            return self.getToken(VenbaParser.UYIR_MEI_O, 0)

        def getRuleIndex(self):
            return VenbaParser.RULE_kuril

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKuril" ):
                listener.enterKuril(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKuril" ):
                listener.exitKuril(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKuril" ):
                return visitor.visitKuril(self)
            else:
                return visitor.visitChildren(self)




    def kuril(self):

        localctx = VenbaParser.KurilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_kuril)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9792144) != 0)):
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


    class NedilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AA_UYIR(self):
            return self.getToken(VenbaParser.AA_UYIR, 0)

        def EE_UYIR(self):
            return self.getToken(VenbaParser.EE_UYIR, 0)

        def OO_UYIR(self):
            return self.getToken(VenbaParser.OO_UYIR, 0)

        def AE_UYIR(self):
            return self.getToken(VenbaParser.AE_UYIR, 0)

        def AI_UYIR(self):
            return self.getToken(VenbaParser.AI_UYIR, 0)

        def OA_UYIR(self):
            return self.getToken(VenbaParser.OA_UYIR, 0)

        def OU_UYIR(self):
            return self.getToken(VenbaParser.OU_UYIR, 0)

        def UYIR_MEI_AA(self):
            return self.getToken(VenbaParser.UYIR_MEI_AA, 0)

        def UYIR_MEI_EE(self):
            return self.getToken(VenbaParser.UYIR_MEI_EE, 0)

        def UYIR_MEI_OO(self):
            return self.getToken(VenbaParser.UYIR_MEI_OO, 0)

        def UYIR_MEI_AE(self):
            return self.getToken(VenbaParser.UYIR_MEI_AE, 0)

        def UYIR_MEI_AI(self):
            return self.getToken(VenbaParser.UYIR_MEI_AI, 0)

        def UYIR_MEI_OA(self):
            return self.getToken(VenbaParser.UYIR_MEI_OA, 0)

        def UYIR_MEI_OU(self):
            return self.getToken(VenbaParser.UYIR_MEI_OU, 0)

        def getRuleIndex(self):
            return VenbaParser.RULE_nedil

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNedil" ):
                listener.enterNedil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNedil" ):
                listener.exitNedil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNedil" ):
                return visitor.visitNedil(self)
            else:
                return visitor.visitChildren(self)




    def nedil(self):

        localctx = VenbaParser.NedilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_nedil)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57316716) != 0)):
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


    class OtruContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEI(self):
            return self.getToken(VenbaParser.MEI, 0)

        def AAYTHAM(self):
            return self.getToken(VenbaParser.AAYTHAM, 0)

        def getRuleIndex(self):
            return VenbaParser.RULE_otru

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtru" ):
                listener.enterOtru(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtru" ):
                listener.exitOtru(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtru" ):
                return visitor.visitOtru(self)
            else:
                return visitor.visitChildren(self)




    def otru(self):

        localctx = VenbaParser.OtruContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_otru)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==1 or _la==26):
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





