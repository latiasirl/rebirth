from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/Pikachuex_57.py"),
              collector_number=47, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")