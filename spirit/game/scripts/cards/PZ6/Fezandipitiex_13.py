from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV065/Fezandipitiex_38.py"),
              collector_number=13, rarity=Rarities.Rare,
              set_code="PZ6", key="PZ6",
              regulation_mark="H")