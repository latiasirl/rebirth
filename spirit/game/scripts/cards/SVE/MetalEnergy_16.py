from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../Free_Energy/MetalEnergy_8.py"),
              collector_number=16, rarity=Rarities.Rare,
              set_code="SVE", key="SVE")