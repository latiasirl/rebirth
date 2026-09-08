from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/BrilliantBlender_164.py"),
              collector_number=52, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8",
              regulation_mark="H")