from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV07/Joltik_50.py"),
               collector_number=24, rarity=Rarities.RareUltra,
               regulation_mark="H")
