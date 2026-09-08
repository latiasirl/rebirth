from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/BosssOrders_154.py"),
               collector_number=47, rarity=Rarities.Rare,
               set_code="PZ4", key="PZ4",
               regulation_mark="G")
