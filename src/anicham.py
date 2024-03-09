from enum import Enum
from typing import Optional

from compiler import parse_script, parse_venba
from visitors.tamizh_visitor_impl import TamizhVisitorImpl
from visitors.venba_visitor_impl import VenbaVisitorImpl


class NodeType(Enum):
    EZHUTTHU = 1
    SOL = 2
    VAAKIYAM = 3
    PATTHI = 4


def get_vaakiyam(patthi_list: list) -> list:
    vaakiyam_list = []
    for patthi in patthi_list:
        vaakiyam_list.extend(patthi)

    return vaakiyam_list


def get_sol(patthi_list: list) -> list:
    sol_list = []
    vaakiyam_list = get_vaakiyam(patthi_list)
    for vaakiyam in vaakiyam_list:
        sol_list.extend(vaakiyam)

    return sol_list


def get_ezhutthu(patthi_list: list) -> list:
    ezhutthu_list = []
    sol_list = get_sol(patthi_list)
    for sol in sol_list:
        ezhutthu_list.extend(sol)

    return ezhutthu_list


def script(string: str, node: Optional[NodeType] = None):
    tree = parse_script(string=string).tamizh_script()
    patthi_list = TamizhVisitorImpl().visit(tree)
    if node == NodeType.SOL:
        return get_sol(patthi_list)
    if node == NodeType.EZHUTTHU:
        return get_ezhutthu(patthi_list)
    if node == NodeType.VAAKIYAM:
        return get_vaakiyam(patthi_list)
    return patthi_list


def venba(string: str):
    tree = parse_venba(string=string).venba()
    return VenbaVisitorImpl().visit(tree)
