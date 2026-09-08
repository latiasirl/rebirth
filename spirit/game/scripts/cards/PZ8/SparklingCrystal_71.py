from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV07/SparklingCrystal_142.py"),
              collector_number=71, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8",
              regulation_mark="H")