from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/Carmine_145.py"),
              collector_number=52, rarity=Rarities.Rare,
              set_code="PZ6", key="PZ6",
              regulation_mark="H")