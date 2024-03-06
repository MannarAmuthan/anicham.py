from anicham import script, NodeType
from visitors.tamizh_visitor_impl import EzhuthuType


def test_should_get_patthigal_from_string():
    actual_data: list = script(
        "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’. இவர் ஒரு சமூக சீர்திருத்தவாதியாக மட்டுமல்லாமல், மிகச்சிறந்த பொருளியல் அறிஞராகவும், அரசியல் தத்துவமேதையாகவும், சமூக சீர்திருத்தவாதியாகவும், பகுத்தறிவு சிந்தனையாளராகவும், சிறந்த எழுத்தாளர் மற்றும் பேச்சாளராகவும், வரலாற்று ஆசானாகவும் விளங்கியவர்.\n" +
        "தலித் இன மக்களுக்கு மட்டுமல்லாமல், ஒடுக்கப்பட்ட மக்களின் வாழ்விருளைப் போக்க, உதித்த சூரியன்.\n" +
        "மகாத்மா காந்திக்கு பிறகு, சுதந்திர இந்தியாவின் மாபெரும் தலைவர் என்று போற்றப்பட்டவர், டாக்டர் அம்பேத்கர் அவர்கள். தன் வாழ்நாள் முழுவதையும் சமூகத்திற்கென அர்ப்பணித்த மாபெரும் சிற்பியான டாக்டர் அம்பேத்கர் அவர்களின் வாழ்க்கை வரலாறு மற்றும் சாதனைகளை காண்போம்.")

    assert len(actual_data) == 3


def test_should_get_vaakiyam_from_patthi():
    actual_data: list = script(
        "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’. இவர் ஒரு சமூக சீர்திருத்தவாதியாக மட்டுமல்லாமல், மிகச்சிறந்த பொருளியல் அறிஞராகவும், அரசியல் தத்துவமேதையாகவும், சமூக சீர்திருத்தவாதியாகவும், பகுத்தறிவு சிந்தனையாளராகவும், சிறந்த எழுத்தாளர் மற்றும் பேச்சாளராகவும், வரலாற்று ஆசானாகவும் விளங்கியவர்")
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
