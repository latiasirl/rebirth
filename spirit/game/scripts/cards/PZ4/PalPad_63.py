from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../XY2/PalPad_92.py"),
               collector_number=63, rarity=Rarities.Rare,
               set_code="PZ4", key="PZ4",
               regulation_mark="G")
