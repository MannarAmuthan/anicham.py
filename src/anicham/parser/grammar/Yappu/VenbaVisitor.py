# Generated from grammar/Yappu/Venba.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VenbaParser import VenbaParser
else:
    from VenbaParser import VenbaParser

# This class defines a complete generic visitor for a parse tree produced by VenbaParser.

class VenbaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VenbaParser#venba.
    def visitVenba(self, ctx:VenbaParser.VenbaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#adi.
    def visitAdi(self, ctx:VenbaParser.AdiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#eetradi.
    def visitEetradi(self, ctx:VenbaParser.EetradiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#seer.
    def visitSeer(self, ctx:VenbaParser.SeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#moovasai.
    def visitMoovasai(self, ctx:VenbaParser.MoovasaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#eerasai.
    def visitEerasai(self, ctx:VenbaParser.EerasaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#themangai.
    def visitThemangai(self, ctx:VenbaParser.ThemangaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#themangani.
    def visitThemangani(self, ctx:VenbaParser.ThemanganiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#pulimangai.
    def visitPulimangai(self, ctx:VenbaParser.PulimangaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#pulimangani.
    def visitPulimangani(self, ctx:VenbaParser.PulimanganiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#koovilangai.
    def visitKoovilangai(self, ctx:VenbaParser.KoovilangaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#koovilangani.
    def visitKoovilangani(self, ctx:VenbaParser.KoovilanganiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#karuvilangai.
    def visitKaruvilangai(self, ctx:VenbaParser.KaruvilangaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#karuvilangani.
    def visitKaruvilangani(self, ctx:VenbaParser.KaruvilanganiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#thema.
    def visitThema(self, ctx:VenbaParser.ThemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#pulima.
    def visitPulima(self, ctx:VenbaParser.PulimaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#koovilam.
    def visitKoovilam(self, ctx:VenbaParser.KoovilamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#karuvilam.
    def visitKaruvilam(self, ctx:VenbaParser.KaruvilamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#eetru_seer.
    def visitEetru_seer(self, ctx:VenbaParser.Eetru_seerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#nirai_asai.
    def visitNirai_asai(self, ctx:VenbaParser.Nirai_asaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#ner_asai.
    def visitNer_asai(self, ctx:VenbaParser.Ner_asaiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#kuril.
    def visitKuril(self, ctx:VenbaParser.KurilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#nedil.
    def visitNedil(self, ctx:VenbaParser.NedilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VenbaParser#otru.
    def visitOtru(self, ctx:VenbaParser.OtruContext):
        return self.visitChildren(ctx)



del VenbaParser