import enum
from typing import List

from parser.grammar.Yappu.VenbaParser import VenbaParser
from parser.grammar.Yappu.VenbaVisitor import VenbaVisitor
from visitors.ast.venba import Venba, Eetradi, Adi, Seer, Eerasai, Moovasai, EerasaiType, MoovasaiType, Ezhutthu, \
    Oasai, Ner, Nirai


class VenbaNodeType(enum.Enum):
    VENBA = 0
    ADI = 1
    EETRADI = 2
    SEER = 3
    MOOVASAI = 4
    EERASAI = 5
    THEMANGAI = 6
    THEMANGANI = 7
    PULIMANGAI = 8
    PULIMANGANI = 9
    KOOVILANGAI = 10
    KOOVILANGANI = 11
    KARUVILANGAI = 12
    KARUVILANGANI = 13
    THEMA = 14
    PULIMA = 15
    KOOVILAM = 16
    KARUVILAM = 17
    EETRU_SEER = 18
    NIRAI_ASAI = 19
    NER_ASAI = 20
    KURIL = 21
    NEDIL = 22
    OTRU = 23


class VenbaVisitorImpl(VenbaVisitor):
    def visitVenba(self, ctx: VenbaParser.VenbaContext):
        adi_list: List[Adi] = []
        adi_contexts = ctx.adi()
        for adi_context in adi_contexts:
            adi_list.append(self.visitAdi(adi_context))
        return Venba(adi_list, self.visitEetradi(ctx.eetradi()))

    def visitAdi(self, ctx: VenbaParser.AdiContext) -> Adi:
        children = []
        for child in ctx.children:
            if child.getText() != ' ':
                children.append(self.visit(child))

        return Adi(children[0], children[1], children[2], children[3])

    def visitEetradi(self, ctx: VenbaParser.EetradiContext) -> Eetradi:
        children = []
        for child in ctx.children:
            if child.getText() != ' ':
                children.append(self.visit(child))

        return Eetradi(children[0], children[1], children[2])

    def visitSeer(self, ctx: VenbaParser.SeerContext) -> Seer:
        child = self.visit(ctx.children[0])
        if isinstance(child, Eerasai):
            return Seer(eerasai=child, moovasai=None)
        return Seer(moovasai=child, eerasai=None)

    def visitEerasai(self, ctx: VenbaParser.EerasaiContext) -> Eerasai:
        return self.visit(ctx.children[0])

    def visitMoovasai(self, ctx: VenbaParser.MoovasaiContext) -> Moovasai:
        return self.visit(ctx.children[0])

    def visitKaruvilam(self, ctx: VenbaParser.KaruvilamContext) -> Eerasai:
        children = self._visit_children(ctx)
        return Eerasai(
            type=EerasaiType.KARUVILAM,
            asai_one=children[0],
            asai_two=children[1]
        )

    def visitKoovilam(self, ctx: VenbaParser.KoovilamContext) -> Eerasai:
        children = self._visit_children(ctx)
        return Eerasai(
            type=EerasaiType.KOOVILAM,
            asai_one=children[0],
            asai_two=children[1]
        )

    def visitThema(self, ctx: VenbaParser.ThemaContext) -> Eerasai:
        children = self._visit_children(ctx)
        return Eerasai(
            type=EerasaiType.THEMA,
            asai_one=children[0],
            asai_two=children[1]
        )

    def visitPulima(self, ctx: VenbaParser.PulimaContext) -> Eerasai:
        children = self._visit_children(ctx)
        return Eerasai(
            type=EerasaiType.PULIMA,
            asai_one=children[0],
            asai_two=children[1]
        )

    def visitKaruvilangai(self, ctx: VenbaParser.KaruvilangaiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.KARUVILANGAI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitKaruvilangani(self, ctx: VenbaParser.KaruvilanganiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.KARUVILANGANI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitPulimangani(self, ctx: VenbaParser.PulimanganiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.PULIMANGANI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitPulimangai(self, ctx: VenbaParser.PulimangaiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.PULIMANGAI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitThemangai(self, ctx: VenbaParser.ThemangaiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.THEMANGAI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitThemangani(self, ctx: VenbaParser.ThemanganiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.THEMANGANI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitKoovilangai(self, ctx: VenbaParser.KoovilangaiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.KOOVILANGAI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitKoovilangani(self, ctx: VenbaParser.KoovilanganiContext) -> Moovasai:
        children = self._visit_children(ctx)
        return Moovasai(
            type=MoovasaiType.KOOVILANGANI,
            asai_one=children[0].asai_one,
            asai_two=children[0].asai_two,
            asai_three=children[1]
        )

    def visitNer_asai(self, ctx: VenbaParser.Ner_asaiContext) -> Ner:
        return Ner(
            ezhutthu_list=self._visit_children(ctx)
        )

    def visitNirai_asai(self, ctx: VenbaParser.Nirai_asaiContext) -> Nirai:
        return Nirai(
            ezhutthu_list=self._visit_children(ctx)
        )

    def visitKuril(self, ctx: VenbaParser.KurilContext) -> Ezhutthu:
        return Ezhutthu(
            letter=self.visit(ctx.getChild(0)),
            oasai=Oasai.KURIL
        )

    def visitNedil(self, ctx: VenbaParser.NedilContext) -> Ezhutthu:
        return Ezhutthu(
            letter=self.visit(ctx.getChild(0)),
            oasai=Oasai.NEDIl
        )

    def visitOtru(self, ctx: VenbaParser.OtruContext) -> Ezhutthu:
        return Ezhutthu(
            letter=self.visit(ctx.getChild(0)),
            oasai=Oasai.OTRU
        )

    def visitTerminal(self, node):
        return node.symbol.text

    def _visit_children(self, ctx):
        children = []
        for child in ctx.children:
            children.append(self.visit(child))

        return children
