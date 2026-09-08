from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/TealMaskOgerponex_25.py"),
              collector_number=53, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")