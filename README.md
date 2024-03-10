# **Anicham(அனிச்சம்)**

Tamizh language parser to parse tamizh texts of UTF-8 encoded. Provides functions for identify and manipulate tamizh strings. Structured by hierchical elements of Tamizh native grammar rules (Ezhuthu, Sol, Vaakiyam). 

## Contents

[1.Core Elements](#core-elements)
- [எழுத்து](#ezhuththu)
- [சொல்](#sol)
- [வாக்கியம்](#vaakiyam)
- [பத்தி](#patthi)

[2.Grammatical Tools](#grammatical-tools)
- [யாப்பு](#yappu)
    - [எழுத்து(ஓசை)](#ezhuththu-oasai)
    - [அசை](#asai)
    - [சீர்](#seer)
    - [அடி](#adi)
    - [வெண்பா](#venba)

[3.Contributing](#contributing)

## **Core elements:**

##### <a id="ezhuththu">எழுத்து(Ezhuththu) - _A Letter_:</a>

A Letter , final smallest entity of all components in a language.
    
Usage:
```python
from anicham import script, NodeType
from anicham import EzhuthuType

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
```

##### <a id="sol">சொல்(Sol) - _A word_:</a>

A word , group of letters(ezhuththu) create Sol.

Usage:
```python      
from anicham import script, NodeType

sol_list: list = script("வெற்றிமாறன், தமிழ் திரைப்பட பிரபல முன்னணி இயக்குனர் ஆவார்",
                        node=NodeType.SOL)
assert len(sol_list) == 7
```


##### <a id="vaakiyam">வாக்கியம்(Vaakiyam) - _A Sentence_:</a>

A sentence , group of words(sorkkal) creates Vaakiyangal.

Usage:
```python       
from anicham import script, NodeType

vaakiyam_list: list = script(
    """வெற்றிமாறன், தமிழ் திரைப்பட பிரபல முன்னணி இயக்குனர் ஆவார். 
    இவர் தமிழ் திரையுலகில் திரைக்கதை எழுத்தாளராக பணியாற்றி அறிமுகமானவர். 
    பின்னர் உதவி இயக்குனராக பிரபல தமிழ் இயக்குனர்களிடம் பணியாற்றி இயக்குனராக அறிமுகமாகி தமிழ் திரையுலகில் புகழ் பெற்றுள்ளார். 
    வெற்றிமாறன் கடலூர் மாவட்டத்தை சேர்ந்தவர்.
    """,
    node=NodeType.VAAKIYAM)
assert len(vaakiyam_list) == 4
```


##### <a id="patthi">பத்தி(Patthi) - _A Paragraph_:</a>

A Paragraph , group of sentences(patthigal) creates Patthi.

Usage:
```python  
from anicham import script   

patthi_list: list = script(
    "விடுதலை இந்தியாவின் முதல் சட்ட அமைச்சராகவும், இந்திய அரசியல் சாசனத்தின் தந்தையாக விளங்கியவர்,‘பீம்ராவ் ராம்ஜி அம்பேத்கர்’. இவர் ஒரு சமூக சீர்திருத்தவாதியாக மட்டுமல்லாமல், மிகச்சிறந்த பொருளியல் அறிஞராகவும், அரசியல் தத்துவமேதையாகவும், சமூக சீர்திருத்தவாதியாகவும், பகுத்தறிவு சிந்தனையாளராகவும், சிறந்த எழுத்தாளர் மற்றும் பேச்சாளராகவும், வரலாற்று ஆசானாகவும் விளங்கியவர்.\n" +
    "தலித் இன மக்களுக்கு மட்டுமல்லாமல், ஒடுக்கப்பட்ட மக்களின் வாழ்விருளைப் போக்க, உதித்த சூரியன்.\n" +
    "மகாத்மா காந்திக்கு பிறகு, சுதந்திர இந்தியாவின் மாபெரும் தலைவர் என்று போற்றப்பட்டவர், டாக்டர் அம்பேத்கர் அவர்கள். தன் வாழ்நாள் முழுவதையும் சமூகத்திற்கென அர்ப்பணித்த மாபெரும் சிற்பியான டாக்டர் அம்பேத்கர் அவர்களின் வாழ்க்கை வரலாறு மற்றும் சாதனைகளை காண்போம்.")

assert len(patthi_list) == 3
```
## **Grammatical Tools:**
### <a id="yappu">யாப்பு(Yappu)</a>

Yappu literally means compilation grammar. It defines semanticity of sound,letter,word,stanza in Tamil poems. 
See more [here](https://ta.wikipedia.org/wiki/%E0%AE%AF%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%B2%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%A3%E0%AE%AE%E0%AF%8D)

##### <a id="ezhuththu-oasai">எழுத்து(ஓசை)(Oasai)</a>
As we see earlier, Ezhuththu is first entity, in yappu , it represents phonetic length form. From the perspective of Phonetics , Tamizh letters catagorized into 3 types.
Kuril, Nedil, Otru (குறில்,நெடில்,ஒற்று).

Usage:
```python
from anicham import yappu_venba,VenbaNodeType,Oasai

ezhutthu_list: list = (
    yappu_venba("சுனை", node=VenbaNodeType.EZHUTTHU))
assert len(ezhutthu_list) == 2
assert ezhutthu_list[0].oasai == Oasai.KURIL
assert ezhutthu_list[0].letter == 'சு'

assert ezhutthu_list[1].oasai == Oasai.NEDIl
assert ezhutthu_list[1].letter == 'னை'
```


##### <a id="asai">அசை(Asai)</a>
Based on Phonetics of letter (Ezhuththu), Asai(sub-part of Word) , is catagorized into 2 types.
Ner,Nirai (நேர்,நிரை). See the grammar file for more info.

Usage:
```python

from anicham import yappu_venba,VenbaNodeType,Nirai,Ner,MoovasaiType


asai_list = yappu_venba("சுரையாழ", node=VenbaNodeType.ASAI)
assert len(asai_list) == 1

assert isinstance(asai_list[0].asai_one, Nirai)
assert isinstance(asai_list[0].asai_two, Ner)
assert isinstance(asai_list[0].asai_three, Ner)

assert asai_list[0].type == MoovasaiType.PULIMANGAI
```

##### <a id="seer">சீர்(Seer)</a>
Based on arrangement of Asai, Tamizh word which is Seer (in Yaapilakkam terminology), is catagorized into 14 types.
First two types contains 1 asai , mostly comes at last point of poetry(called eetru-seer).
Next 4 types contains 2 asai inside, so They are called Eerasai Seer (2 Asai Seer).
and last 8 types contains 3 asai inside so,  They are called Moovasai Seer (3 Asai Seer). 
Read about all types [here](https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AF%80%E0%AE%B0%E0%AF%8D_(%E0%AE%AF%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%B2%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%A3%E0%AE%AE%E0%AF%8D)#%E0%AE%9A%E0%AF%80%E0%AE%B0%E0%AF%8D_%E0%AE%B5%E0%AE%95%E0%AF%88%E0%AE%95%E0%AE%B3%E0%AF%8D)

Usage:
```python

from anicham import yappu_venba,VenbaNodeType,EerasaiType

seer_list: list= yappu_venba("இன்றுகொல்", node=VenbaNodeType.SEER)

assert len(seer_list) == 1

assert seer_list[0].eerasai.type == EerasaiType.KOOVILAM
```

##### <a id="adi">அடி(Adi)</a>
Basically it means line of poem. Adi contains 4 seer. 
Last line of the poem is called "Eetradi", which contains 3 seer. Last seer is known as eetru-seer.
Read more [here](https://ta.wikipedia.org/wiki/%E0%AE%85%E0%AE%9F%E0%AE%BF_(%E0%AE%AF%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%B2%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%A3%E0%AE%AE%E0%AF%8D,_%E0%AE%9A%E0%AF%80%E0%AE%B0%E0%AF%8D_%E0%AE%8E%E0%AE%A3%E0%AF%8D%E0%AE%A3%E0%AE%BF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%88)).

Usage:
```python
from anicham import yappu_venba,VenbaNodeType

adi_list  = yappu_venba("""அரிய வரைகீண்டு காட்டுவார் யாரே""", node=VenbaNodeType.ADI)

assert len(adi_list) == 1
assert len(adi_list[0].seer_list) == 4
```

##### <a id="venba">வெண்பா(Venba)</a>
Venba is a form of classical Tamil poetry. Which is the root of all above elements, and define their rules. 
You can provide Venba poems as input , and it will be parsed like below.
Read more about [here](https://ta.wikipedia.org/wiki/%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AA%E0%AE%BE#%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AA%E0%AE%BE%E0%AE%B5%E0%AF%81%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%BE%E0%AE%A9_%E0%AE%AF%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%B2%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%A3%E0%AE%AE%E0%AF%8D)

Usage:
```python
from anicham import yappu_venba,EerasaiType,MoovasaiType,Venba,EetruSeerAsai

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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.