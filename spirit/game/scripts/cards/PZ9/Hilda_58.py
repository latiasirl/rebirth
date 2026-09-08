from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../RSV10PT5/Hilda_84.py"),
              collector_number=58, rarity=Rarities.Rare,
              set_code="PZ9", key="PZ9",
              regulation_mark="I")