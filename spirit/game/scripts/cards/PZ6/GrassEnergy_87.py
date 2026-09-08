from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../Free_Energy/GrassEnergy_1.py"),
              collector_number=87, rarity=Rarities.Rare,
              set_code="PZ6", key="PZ6")