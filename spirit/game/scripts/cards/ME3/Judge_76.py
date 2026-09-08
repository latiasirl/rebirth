from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../HGSS2/Judge_78.py"),
               collector_number=76, rarity=Rarities.Uncommon,
               set_code="ME3", key="ME3",
               regulation_mark="J")
