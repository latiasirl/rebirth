from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME1/MegaSignal_121.py"),
              collector_number=64, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8",
              regulation_mark="I")