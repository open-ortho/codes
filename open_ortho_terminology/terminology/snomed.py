""" snomed: a collection of static SNOMED-CT codes.

Used whenever a code is necessary, for various implementations.

"""
from . import Code

PREFIX = "SCT"
SYSTEM = "http://snomed.info/sct"

class SnomedCode(Code):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.prefix = PREFIX
        self.system = SYSTEM

dental_chair = SnomedCode(
    code='706356006',
    display='Dental examination/treatment chair')

orthod_treatment_perm_class1 = SnomedCode(
    code='3891000',
    display='Comprehensive orthodontic treatment, permanent dentition, for class I malocclusion')

ortho_treatment = SnomedCode(
    code='122452007',
    display='Comprehensive orthodontic treatment')

orthodontist = SnomedCode(
    code='37504001',
    display='Orthodontist')

clinical_staff = SnomedCode(
    code='4162009',
    display='Dental assistant')

admin_staff = SnomedCode(
    code='224608005',
    display='Administrative healthcare staff')

tech_support = SnomedCode(
    code='159324001',
    display='Technical assistant')

EV01 = SnomedCode(
    code='1306623000',
    display="Photographic extraoral image of right half of face with lips relaxed and teeth in centric occlusion (record artifact)",
    synonyms=['EV-01', 'EO.RP.LR.CO'])
""" Used for ... """


EV02 = SnomedCode(
    code='1306622005',
    display="Photographic extraoral image of right half of face with lips relaxed and jaws in centric relation (record artifact)",
    synonyms=['EV-02', 'EO.RP.LR.CR'])
""" Used for ... """


EV15 = SnomedCode(
    code='1306630006',
    display="Photographic extraoral image of full face with lips relaxed and teeth in centric occlusion (record artifact)",
    synonyms=['EV-15', 'EO.FF.LR.CO'])
""" Used for ... """


EV17 = SnomedCode(
    code='1306622005',
    display="Photographic extraoral image of full face with lips closed and teeth in centric occlusion (record artifact)",
    synonyms=['EV-17', 'EO.FF.LC.CO'])
""" Used for ... """


EV19 = SnomedCode(
    code='1306622005',
    display="Photographic extraoral image of full face with full smile and teeth in centric occlusion (record artifact)",
    synonyms=['EV-19', 'EO.FF.FS.CO'])
""" Used for ... """

