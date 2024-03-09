from enum import Enum
from typing import Optional, List, Union


from .visitors.ast.venba import Venba, Adi, Seer, Eetradi, EetruSeer, Eerasai, Moovasai, Ezhutthu, Nirai, Ner, \
    MoovasaiType,EerasaiType
from .visitors.tamizh_visitor_impl import TamizhVisitorImpl, EzhuthuType
from .visitors.venba_visitor_impl import VenbaVisitorImpl
from .compiler import parse_script, parse_venba


class NodeType(Enum):
    EZHUTTHU = 1
    SOL = 2
    VAAKIYAM = 3
    PATTHI = 4


class VenbaNodeType(Enum):
    EZHUTTHU = 1
    ASAI = 2
    SEER = 3
    ADI = 4
    VENBA = 5


def script(string: str, node: Optional[NodeType] = None):
    tree = parse_script(string=string).tamizh_script()
    patthi_list = TamizhVisitorImpl().visit(tree)
    if node == NodeType.SOL:
        return _get_sol(patthi_list)
    if node == NodeType.EZHUTTHU:
        return _get_ezhutthu(patthi_list)
    if node == NodeType.VAAKIYAM:
        return _get_vaakiyam(patthi_list)
    return patthi_list


def yappu_venba(string: str, node: Optional[VenbaNodeType] = None):
    venba_visitor_impl = VenbaVisitorImpl()
    if node == VenbaNodeType.ADI:
        return _get_adi(venba_visitor_impl.visit(parse_venba(string=string).venba()))
    if node == VenbaNodeType.SEER:
        return _get_seer(venba_visitor_impl.visit(parse_venba(string=string).venba()))
    if node == VenbaNodeType.ASAI:
        return _get_asai(venba_visitor_impl.visit(parse_venba(string=string).venba()))
    if node == VenbaNodeType.EZHUTTHU:
        return _get_ezhutthu_venba(venba_visitor_impl.visit(parse_venba(string=string).venba()))
    return VenbaVisitorImpl().visit(parse_venba(string=string).venba())


def _get_vaakiyam(patthi_list: list) -> list:
    vaakiyam_list = []
    for patthi in patthi_list:
        vaakiyam_list.extend(patthi)

    return vaakiyam_list


def _get_sol(patthi_list: list) -> list:
    sol_list = []
    vaakiyam_list = _get_vaakiyam(patthi_list)
    for vaakiyam in vaakiyam_list:
        sol_list.extend(vaakiyam)

    return sol_list


def _get_ezhutthu(patthi_list: list) -> list:
    ezhutthu_list = []
    sol_list = _get_sol(patthi_list)
    for sol in sol_list:
        ezhutthu_list.extend(sol)

    return ezhutthu_list


def _get_adi(venba: Venba) -> List[Union[Adi, Eetradi]]:
    adi_list = []
    if venba.adi_list:
        adi_list.extend(venba.adi_list)
    if venba.eetradi:
        adi_list.append(venba.eetradi)
    return adi_list


def _get_seer(venba: Venba) -> List[Union[Seer, EetruSeer]]:
    adi_list: List[Union[Adi, Eetradi]] = _get_adi(venba)
    seer_list = []
    for adi in adi_list:
        if isinstance(adi, Adi):
            seer_list.extend(adi.seer_list)
        if isinstance(adi, Eetradi):
            seer_list.extend(adi.seer_list)

    return seer_list


def _get_asai(venba: Venba) -> List[Union[Eerasai, Moovasai]]:
    seer_list: List[Union[Seer, EetruSeer]] = _get_seer(venba)
    asai_list = []
    for seer in seer_list:
        if isinstance(seer, Seer):
            if seer.eerasai:
                asai_list.append(seer.eerasai)
            else:
                asai_list.append(seer.moovasai)
        if isinstance(seer, EetruSeer):
            seer_list.append(seer.asai)

    return asai_list


def _get_ezhutthu_venba(venba: Venba) -> List[Ezhutthu]:
    asai_list: List[Union[Eerasai, Moovasai]] = _get_asai(venba)
    ezhutthu_list = []
    for asai in asai_list:
        if isinstance(asai, Eerasai):
            ezhutthu_list.extend(asai.asai_one.ezhutthu_list)
            ezhutthu_list.extend(asai.asai_two.ezhutthu_list)
        if isinstance(asai, Moovasai):
            ezhutthu_list.extend(asai.asai_one.ezhutthu_list)
            ezhutthu_list.extend(asai.asai_two.ezhutthu_list)
            ezhutthu_list.extend(asai.asai_three.ezhutthu_list)

    return ezhutthu_list
