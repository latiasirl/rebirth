from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV065/Powerglass_63.py"),
              collector_number=84, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="H")