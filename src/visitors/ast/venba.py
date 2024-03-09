from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Union, Tuple


class Oasai(Enum):
    KURIL = 1
    NEDIl = 2
    OTRU = 3


@dataclass
class Ezhutthu:
    letter: str
    oasai: Oasai


@dataclass
class Ner:
    ezhutthu_list: List[Ezhutthu]


@dataclass
class Nirai:
    ezhutthu_list: List[Ezhutthu]


class EerasaiType(Enum):
    THEMA = 1
    PULIMA = 2
    KARUVILAM = 3
    KOOVILAM = 4


class MoovasaiType(Enum):
    THEMANGAI = 1
    PULIMANGAI = 2
    KOOVILANGAI = 3
    KARUVILANGAI = 4
    THEMANGANI = 5
    PULIMANGANI = 6
    KOOVILANGANI = 7
    KARUVILANGANI = 8


@dataclass
class Eerasai:
    asai_one: Union[Ner, Nirai]
    asai_two: Union[Ner, Nirai]
    type: EerasaiType


@dataclass
class Moovasai:
    asai_one: Union[Ner, Nirai]
    asai_two: Union[Ner, Nirai]
    asai_three: Union[Ner, Nirai]
    type: MoovasaiType


@dataclass
class Seer:
    eerasai: Optional[Eerasai]
    moovasai: Optional[Moovasai]


@dataclass
class EetruSeer:
    seer: Union[Ner, Nirai, Eerasai]


@dataclass
class Eetradi:
    seer_one: Seer
    seer_two: Seer
    eetru_seer: EetruSeer


@dataclass
class Adi:
    seer_one: Seer
    seer_two: Seer
    seer_three: Seer
    seer_four: Seer


@dataclass
class Venba:
    adi_list: List[Adi]
    eetradi: Eetradi
