""" open_ortho: a collection of static open-ortho.org codes.

Used whenever a code is necessary, for various implementations.
"""
from fhir.resources.coding import Coding

from open_ortho_terminology.terminology import Code
from open_ortho_terminology.terminology.snomed import EV01, EV15, EV19
PREFIX = 'OPOR'


class NAMESPACES:
    root_uid = "1.3.6.1.4.1.61741.11.3"
    url = "http://open-ortho.org/terminology"


def make_code(s):
    """
    Convert a string of ASCII characters to a single string of their equivalent integer values concatenated together.

    Args:
    s (str): A string to convert.

    Returns:
    str: A string consisting of the ASCII integer values concatenated together without any spaces.
    """
    # Convert each character to its ASCII integer, then to a string, and concatenate
    return ''.join(str(ord(char)) for char in s)


class OpenOrthoCode(Code):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prefix = PREFIX
        self.system = NAMESPACES.url


EV07 = OpenOrthoCode(
    code=f"{make_code('EV07')}",
    display="Extraoral, Right Profile (subject is facing observer's right), Mandible Postured Forward",
    synonyms=['EV-07', 'EO.RP.MD.PF'])
""" Used for ... """

EV28 = OpenOrthoCode(
    code=f"{make_code('EV28')}",
    display="Extraoral, Left Profile (subject is facing observer's left), Mandible Postured Forward",
    synonyms=['EV-28', 'EO.LP.MD.PF'])
""" Used for ... """

IV01 = OpenOrthoCode(
    code=f"{make_code('IV01')}",
    display='Intraoral Right Buccal Segment, Centric Occlusion, Direct View',
    synonyms=['IV-01', 'IO.RB.CO'])
""" Used for ... """

IV02 = OpenOrthoCode(
    code=f"{make_code('IV02')}",
    display='Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror',
    synonyms=['IV-02', 'IO.RB.CO.WM'])
""" Used for ... """

IV03 = OpenOrthoCode(
    code=f"{make_code('IV03')}",
    display='Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror, But Corrected',
    synonyms=['IV-03', 'IO.RB.CO.WM.BC'])
""" Used for ... """

IV04 = OpenOrthoCode(
    code=f"{make_code('IV04')}",
    display='Intraoral, Right Buccal Segment, Centric Relation (Direct View)',
    synonyms=['IV-04', 'IO.RB.CR'])
""" Used for ... """

IV05 = OpenOrthoCode(
    code=f"{make_code('IV05')}",
    display='Intraoral, Right Buccal Segment, Centric Relation, With Mirror',
    synonyms=['IV-05', 'IO.RB.CR.WM'])
""" Used for ... """

IV06 = OpenOrthoCode(
    code=f"{make_code('IV06')}",
    display='Intraoral, Right Buccal Segment, Centric Relation, With Mirror, But Corrected',
    synonyms=['IV-06', 'IO.RB.CR.WM.BC'])
""" Used for ... """

IV07 = OpenOrthoCode(
    code=f"{make_code('IV07')}",
    display='Intraoral, Frontal View, Centric Occlusion',
    synonyms=['IV-07', 'IO.FV.CO'])
""" Used for ... """

IV08 = OpenOrthoCode(
    code=f"{make_code('IV08')}",
    display='Intraoral, Frontal View, Centric Relation',
    synonyms=['IV-08', 'IO.FV.CR'])
""" Used for ... """

IV09 = OpenOrthoCode(
    code=f"{make_code('IV09')}",
    display='Intraoral, Frontal View, Teeth Apart',
    synonyms=['IV-09', 'IO.FV.TA'])
""" Used for ... """

IV10 = OpenOrthoCode(
    code=f"{make_code('IV10')}",
    display='Intraoral, Frontal View, Mouth Open',
    synonyms=['IV-10', 'IO.FV.MO'])
""" Used for ... """

IV11 = OpenOrthoCode(
    code=f"{make_code('IV11')}",
    display='Intraoral, Frontal View Inferior (showing depth of bite and overjet), Centric Occlusion',
    synonyms=['IV-11', 'IO.FV.IV.CO'])
""" Used for ... """

IV12 = OpenOrthoCode(
    code=f"{make_code('IV12')}",
    display='Intraoral, Frontal View Inferior (showing depth of bite and overjet), Centric Relation',
    synonyms=['IV-12', 'IO.FV.IV.CR'])
""" Used for ... """

IV13 = OpenOrthoCode(
    code=f"{make_code('IV13')}",
    display='Intraoral, Frontal View, showing Tongue Thrust',
    synonyms=['IV-13', 'IO.FV.TT.NM'])
""" Used for ... """

IV14 = OpenOrthoCode(
    code=f"{make_code('IV14')}",
    display='Intraoral, Right Lateral View, Centric Occlusion, showing Overjet, (Direct View showing overjet from the side)',
    synonyms=['IV-14', 'IO.RL.CO.OJ'])
""" Used for ... """

IV15 = OpenOrthoCode(
    code=f"{make_code('IV15')}",
    display='Intraoral, Right Lateral View, Centric Relation, showing Overjet (Direct View showing overjet from the side)',
    synonyms=['IV-15', 'IO.RL.CR.OJ'])
""" Used for ... """

IV16 = OpenOrthoCode(
    code=f"{make_code('IV16')}",
    display='Intraoral, Left Lateral View, Centric Occlusion, showing Overjet, (Direct View showing overjet from the side)',
    synonyms=['IV-16', 'IO.LL.CO.OJ'])
""" Used for ... """

IV17 = OpenOrthoCode(
    code=f"{make_code('IV17')}",
    display='Intraoral, Left Lateral View, Centric Relation, showing Overjet (Direct View showing overjet from the side)',
    synonyms=['IV-17', 'IO.LL.CR.OJ'])
""" Used for ... """


IV18 = OpenOrthoCode(
    code=f"{make_code('IV18')}",
    display='Intraoral, Left Buccal Segment, Centric Occlusion (Direct View)',
    synonyms=['IV-18', 'IO.LB.CO'])
""" Used for ... """


IV19 = OpenOrthoCode(
    code=f"{make_code('IV19')}",
    display='Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror',
    synonyms=['IV-19', 'IO.LB.CO.WM'])
""" Used for ... """


IV20 = OpenOrthoCode(
    code=f"{make_code('IV20')}",
    display='Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror, But Corrected',
    synonyms=['IV-20', 'IO.LB.CO.WM.BC'])
""" Used for ... """


IV21 = OpenOrthoCode(
    code=f"{make_code('IV21')}",
    display='Intraoral, Left Buccal Segment, Centric Relation (Direct View)',
    synonyms=['IV-21', 'IO.LB.CR'])
""" Used for ... """


IV22 = OpenOrthoCode(
    code=f"{make_code('IV22')}",
    display='Intraoral, Left Buccal Segment, Centric Relation, With Mirror',
    synonyms=['IV-22', 'IO.LB.CR.WM'])
""" Used for ... """


IV23 = OpenOrthoCode(
    code=f"{make_code('IV23')}",
    display='Intraoral, Left Buccal Segment, Centric Relation, With Mirror, But Corrected',
    synonyms=['IV-23', 'IO.LB.CR.WM.BC'])
""" Used for ... """


IV24 = OpenOrthoCode(
    code=f"{make_code('IV24')}",
    display='Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror',
    synonyms=['IV-24', 'IO.MX.MO.OV.WM'])
""" Used for ... """


IV25 = OpenOrthoCode(
    code=f"{make_code('IV25')}",
    display='Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected',
    synonyms=['IV-25', 'IO.MX.MO.OV.WM.BC'])
""" Used for ... """


IV26 = OpenOrthoCode(
    code=f"{make_code('IV26')}",
    display='Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror',
    synonyms=['IV-26', 'IO.MD.MO.OV.WM'])
""" Used for ... """


IV27 = OpenOrthoCode(
    code=f"{make_code('IV27')}",
    display='Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror, But Corrected',
    synonyms=['IV-27', 'IO.MD.MO.OV.WM.BC'])
""" Used for ... """


IV28 = OpenOrthoCode(
    code=f"{make_code('IV28')}",
    display='Intraoral, showing Gingival Recession (ISO tooth numbers)',
    synonyms=['IV-28', 'IO.GR.[tooth number]'])
""" Used for ... """


IV29 = OpenOrthoCode(
    code=f"{make_code('IV29')}",
    display='Intraoral, showing Frenum (ISO tooth numbers)',
    synonyms=['IV-29', 'IO.FR.[tooth number]'])
""" Used for ... """


IV30 = OpenOrthoCode(
    code=f"{make_code('IV30')}",
    display='Intraoral, any photo using a photo accessory device (modifiers)',
    synonyms=['IV-30', 'IO.[modifier].PA'])
""" Used for ... """


VS01 = OpenOrthoCode(
    code=f"{make_code('VS01')}",
    display='ViewSet 01',
    synonyms=['VS-01', 'ABO'],
    views=[[EV01], [EV15], [EV19], [IV25], [None],
           [IV27], [IV01, IV03], [IV07], [IV18, IV20]]
)
