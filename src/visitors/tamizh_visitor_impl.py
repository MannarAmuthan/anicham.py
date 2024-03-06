from enum import Enum

from parser.grammar.TamizhParser import TamizhParser
from parser.grammar.TamizhVisitor import TamizhVisitor


class EzhuthuType(Enum):
    MEI = 1
    UYIR_MEI_OU = 2
    UYIR_MEI_OA = 3
    UYIR_MEI_O = 4
    UYIR_MEI_AI = 5
    UYIR_MEI_AE = 6
    UYIR_MEI_E = 7
    UYIR_MEI_OO = 8
    UYIR_MEI_U = 9
    UYIR_MEI_EE = 10
    UYIR_MEI_I = 11
    UYIR_MEI_AA = 12
    UYIR_MEI_A = 13
    UYIR = 14
    PULLI = 15
    KAAL = 16
    SULI = 17
    NEDIL_SULI = 18
    U_KURIL = 19
    U_NEDIL = 20
    EA_KURIL = 21
    EA_NEDIL = 22
    I = 23
    O_KURIL = 24
    O_NEDIL = 25
    OU = 26
    AAYTHAM = 27
    GRANTHA_SRI = 28
    GRANTHA_MEI = 29
    GRANTHA_OU = 30
    GRANTHA_OA = 31
    GRANTHA_O = 32
    GRANTHA_AI = 33
    GRANTHA_AE = 34
    GRANTHA_E = 35
    GRANTHA_OO = 36
    GRANTHA_U = 37
    GRANTHA_EE = 38
    GRANTHA_I = 39
    GRANTHA_AA = 40
    GRANTHA_A = 41
    GRANTHA_JA = 42
    GRANTHA_SH = 43
    GRANTHA_SS = 44
    GRANTHA_S = 45
    GRANTHA_H = 46


class TamizhVisitorImpl(TamizhVisitor):

    def visitTamizh_script(self, ctx: TamizhParser.Tamizh_scriptContext):
        patthi_list = []
        for patthi_ctx in ctx.patthi():
            patthi_list.append(self.visitPatthi(patthi_ctx))
        return patthi_list

    def visitPatthi(self, ctx: TamizhParser.PatthiContext):
        vaakiyam_list = []
        for vaakiyam_ctx in ctx.vaakiyam():
            vaakiyam_list.append(self.visitVaakiyam(vaakiyam_ctx))
        return vaakiyam_list

    def visitVaakiyam(self, ctx: TamizhParser.VaakiyamContext):
        sol_list = []
        for sol_ctx in ctx.sol():
            sol_list.append(self.visitSol(sol_ctx))
        return sol_list

    def visitSol(self, ctx: TamizhParser.SolContext):
        sol_list = []
        for ezhuththu_ctx in ctx.ezhuththu():
            sol_list.append(self.visitEzhuththu(ezhuththu_ctx))
        return sol_list

    def visitEzhuththu(self, ctx: TamizhParser.EzhuththuContext):
        return self.visit(ctx.getChild(0))

    def visitTerminal(self, node):
        return node.symbol.text, EzhuthuType(node.symbol.type)
