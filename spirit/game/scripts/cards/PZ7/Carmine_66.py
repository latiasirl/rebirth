from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/Carmine_145.py"),
              collector_number=66, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")