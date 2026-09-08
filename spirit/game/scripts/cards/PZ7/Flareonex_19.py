from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV085/Flareonex_14.py"),
              collector_number=19, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")