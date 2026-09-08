from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SS/RareCandy_88.py"),
               collector_number=141, rarity=Rarities.Uncommon,
               set_code="CZ", key="CZ",
               regulation_mark="F")
