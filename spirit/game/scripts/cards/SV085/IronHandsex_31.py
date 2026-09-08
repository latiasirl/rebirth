from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV4/IronHandsex_70.py"),
               collector_number=31, rarity=Rarities.RareHoloEX,
               regulation_mark="H")
