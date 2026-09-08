from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/BiancasDevotion_142.py"),
              collector_number=60, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")