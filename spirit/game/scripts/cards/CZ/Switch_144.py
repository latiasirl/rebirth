from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../BASE1/Switch_95.py"),
               collector_number=144, rarity=Rarities.Common,
               set_code="CZ", key="CZ",
               regulation_mark="F")
