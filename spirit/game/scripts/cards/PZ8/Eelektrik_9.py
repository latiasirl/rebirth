from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ZSV10PT5/Eelektrik_31.py"),
              collector_number=9, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8",
              regulation_mark="I")