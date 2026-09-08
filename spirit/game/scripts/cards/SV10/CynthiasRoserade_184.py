from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV10/CynthiasRoserade_8.py"),
               collector_number=184, rarity=Rarities.RareUltra,
               set_code="SV10", key="SV10",
               regulation_mark="I")
