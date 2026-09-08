from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../HGSS2/Judge_78.py"),
               collector_number=222, rarity=Rarities.RareUltra,
               set_code="SV10", key="SV10",
               regulation_mark="G")
