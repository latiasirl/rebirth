from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV3PT5/Charmander_4.py"),
               collector_number=7, rarity=Rarities.Common,
               set_code="SV4PT5", key="SV4PT5",
               regulation_mark="G")
