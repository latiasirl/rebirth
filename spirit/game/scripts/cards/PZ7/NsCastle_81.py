from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV09/NsCastle_152.py"),
              collector_number=81, rarity=Rarities.Rare,
              set_code="PZ7", key="PZ7",
              regulation_mark="I")