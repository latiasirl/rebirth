from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../HGSS2/Judge_78.py"),
               collector_number=58, rarity=Rarities.Rare,
               set_code="PZ4", key="PZ4",
               regulation_mark="G")
