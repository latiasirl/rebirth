from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../BW5/UltraBall_102.py"),
               collector_number=146, rarity=Rarities.Uncommon,
               set_code="CZ", key="CZ",
               regulation_mark="F")
