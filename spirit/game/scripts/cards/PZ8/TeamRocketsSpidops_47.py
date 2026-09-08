from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV10/TeamRocketsSpidops_20.py"),
              collector_number=47, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8",
              regulation_mark="I")