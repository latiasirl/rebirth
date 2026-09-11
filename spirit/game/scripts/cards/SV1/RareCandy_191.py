from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SS/RareCandy_88.py"),
               collector_number=191, rarity=Rarities.Common,
               set_code="SV1", key="SV1",
               regulation_mark="G")
