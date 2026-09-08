from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/MistEnergy_161.py"),
               collector_number=76, rarity=Rarities.Rare,
               set_code="PZ5", key="PZ5",
               regulation_mark="H")
