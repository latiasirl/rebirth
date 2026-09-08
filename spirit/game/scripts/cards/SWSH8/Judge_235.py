from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../HGSS2/Judge_78.py"),
               collector_number=235, rarity=Rarities.Uncommon,
               set_code="SWSH8", key="SWSH8",
               regulation_mark="E")
