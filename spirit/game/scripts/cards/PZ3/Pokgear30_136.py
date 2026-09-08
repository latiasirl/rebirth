from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../HGSS1/Pokgear30_96.py"),
               collector_number=136, rarity=Rarities.Rare,
               set_code="PZ3", key="PZ3",
               regulation_mark="G")
