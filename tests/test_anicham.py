from typing import List, Union

from anicham import script, NodeType, VenbaNodeType, yappu_venba, EzhuthuType, MoovasaiType, Ezhutthu, EetruSeerAsai
from anicham import Oasai, Nirai, Moovasai, Ner, Eerasai, EerasaiType, Seer, Adi, Venba


def test_should_get_patthigal_from_string():
    actual_data: list = script(
        "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’. இவர் ஒரு சமூக சீர்திருத்தவாதியாக மட்டுமல்லாமல், மிகச்சிறந்த பொருளியல் அறிஞராகவும், அரசியல் தத்துவமேதையாகவும், சமூக சீர்திருத்தவாதியாகவும், பகுத்தறிவு சிந்தனையாளராகவும், சிறந்த எழுத்தாளர் மற்றும் பேச்சாளராகவும், வரலாற்று ஆசானாகவும் விளங்கியவர்.\n" +
        "தலித் இன மக்களுக்கு மட்டுமல்லாமல், ஒடுக்கப்பட்ட மக்களின் வாழ்விருளைப் போக்க, உதித்த சூரியன்.\n" +
        "மகாத்மா காந்திக்கு பிறகு, சுதந்திர இந்தியாவின் மாபெரும் தலைவர் என்று போற்றப்பட்டவர், டாக்டர் அம்பேத்கர் அவர்கள். தன் வாழ்நாள் முழுவதையும் சமூகத்திற்கென அர்ப்பணித்த மாபெரும் சிற்பியான டாக்டர் அம்பேத்கர் அவர்களின் வாழ்க்கை வரலாறு மற்றும் சாதனைகளை காண்போம்.")

    assert len(actual_data) == 3


def test_should_get_vaakiyam_from_patthi():
    actual_data: list = script(
        "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’. "
        "இவர் ஒரு சமூக சீர்திருத்தவாதியாக மட்டுமல்லாமல், மிகச்சிறந்த பொருளியல் அறிஞராகவும், அரசியல் தத்துவமேதையாகவும், "
        "சமூக சீர்திருத்தவாதியாகவும், பகுத்தறிவு சிந்தனையாளராகவும், சிறந்த எழுத்தாளர் மற்றும் பேச்சாளராகவும், வரலாற்று ஆசானாகவும் விளங்கியவர்")
    assert len(actual_data[0]) == 2


def test_should_get_sorkkal_from_vaakiyam():
    actual_data: list = script(
        "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’.")
    assert len(actual_data[0][0]) == 13


def test_should_get_ezhuthu_from_sol():
    actual_data: list = script("அறத்துப்பால்")
    assert len(actual_data[0][0][0]) == 7

    assert actual_data[0][0][0][0][1] == EzhuthuType.UYIR
    assert actual_data[0][0][0][1][1] == EzhuthuType.UYIR_MEI_A
    assert actual_data[0][0][0][2][1] == EzhuthuType.MEI
    assert actual_data[0][0][0][3][1] == EzhuthuType.UYIR_MEI_U
    assert actual_data[0][0][0][4][1] == EzhuthuType.MEI
    assert actual_data[0][0][0][5][1] == EzhuthuType.UYIR_MEI_AA
    assert actual_data[0][0][0][6][1] == EzhuthuType.MEI


def test_should_vaakiyam_list():
    vaakiyam_list: list = script(
        """வெற்றிமாறன், தமிழ் திரைப்பட பிரபல முன்னணி இயக்குனர் ஆவார். 
        இவர் தமிழ் திரையுலகில் திரைக்கதை எழுத்தாளராக பணியாற்றி அறிமுகமானவர். 
        பின்னர் உதவி இயக்குனராக பிரபல தமிழ் இயக்குனர்களிடம் பணியாற்றி இயக்குனராக அறிமுகமாகி தமிழ் திரையுலகில் புகழ் பெற்றுள்ளார். 
        வெற்றிமாறன் கடலூர் மாவட்டத்தை சேர்ந்தவர்.
        """,
        node=NodeType.VAAKIYAM)
    assert len(vaakiyam_list) == 4


def test_should_get_sol_list():
    sol_list: list = script(
        """வெற்றிமாறன், தமிழ் திரைப்பட பிரபல முன்னணி இயக்குனர் ஆவார். 
        இவர் தமிழ் திரையுலகில் திரைக்கதை எழுத்தாளராக பணியாற்றி அறிமுகமானவர். 
        பின்னர் உதவி இயக்குனராக பிரபல தமிழ் இயக்குனர்களிடம் பணியாற்றி இயக்குனராக அறிமுகமாகி தமிழ் திரையுலகில் புகழ் பெற்றுள்ளார். 
        வெற்றிமாறன் கடலூர் மாவட்டத்தை சேர்ந்தவர்.
        """,
        node=NodeType.SOL)
    assert len(sol_list) == 31


def test_should_get_ezhutthu_list():
    ezhutthu_list: list = script('ஜவஹர்லால் நேரு', node=NodeType.EZHUTTHU)
    assert len(ezhutthu_list) == 8

    assert ezhutthu_list == [('ஜ', EzhuthuType.GRANTHA_A),
                             ('வ', EzhuthuType.UYIR_MEI_A),
                             ('ஹ', EzhuthuType.GRANTHA_A),
                             ('ர்', EzhuthuType.MEI),
                             ('லா', EzhuthuType.UYIR_MEI_AA),
                             ('ல்', EzhuthuType.MEI),
                             ('நே', EzhuthuType.UYIR_MEI_AE),
                             ('ரு', EzhuthuType.UYIR_MEI_U)]


def test_should_get_venba():
    actual: Venba = yappu_venba("உடுக்கை இழந்தவன் கைபோல ஆங்கே\n" + "இடுக்கண் களைவதாம் நட்பு")
    assert len(actual.adi_list) == 1

    assert actual.adi_list[0].seer_list[0].eerasai.type == EerasaiType.PULIMA
    assert actual.adi_list[0].seer_list[1].eerasai.type == EerasaiType.KARUVILAM
    assert actual.adi_list[0].seer_list[2].moovasai.type == MoovasaiType.THEMANGAI
    assert actual.adi_list[0].seer_list[3].eerasai.type == EerasaiType.THEMA

    assert actual.eetradi.seer_list[0].eerasai.type == EerasaiType.PULIMA
    assert actual.eetradi.seer_list[1].eerasai.type == EerasaiType.KARUVILAM
    assert actual.eetradi.seer_list[2].asai.type == EerasaiType.THEMA

    assert actual.eetradi.seer_list[2].get_eetru_seer_asai() == EetruSeerAsai.KAASU


def test_should_get_adi():
    adi_list: List[Adi] = yappu_venba("""அரிய வரைகீண்டு காட்டுவார் யாரே""", node=VenbaNodeType.ADI)

    assert len(adi_list) == 1
    assert len(adi_list[0].seer_list) == 4


def test_should_get_seer_list():
    seer_list: List[Seer] = yappu_venba("இன்றுகொல்", node=VenbaNodeType.SEER)

    assert len(seer_list) == 1
    assert seer_list[0].eerasai.type == EerasaiType.KOOVILAM


def test_should_get_asai_list():
    asai_list: List[Union[Eerasai, Moovasai]] = (
        yappu_venba("சுரையாழ", node=VenbaNodeType.ASAI))
    assert len(asai_list) == 1
    assert isinstance(asai_list[0].asai_one, Nirai)
    assert isinstance(asai_list[0].asai_two, Ner)
    assert isinstance(asai_list[0].asai_three, Ner)
    assert asai_list[0].type == MoovasaiType.PULIMANGAI


def test_should_get_venba_ezhutthu_list():
    ezhutthu_list: List[Ezhutthu] = (
        yappu_venba("சுனை", node=VenbaNodeType.EZHUTTHU))
    assert len(ezhutthu_list) == 2
    assert ezhutthu_list[0].oasai == Oasai.KURIL
    assert ezhutthu_list[0].letter == 'சு'

    assert ezhutthu_list[1].oasai == Oasai.NEDIl
    assert ezhutthu_list[1].letter == 'னை'
