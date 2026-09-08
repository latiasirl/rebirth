from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Eri_146.py"),
               collector_number=210, rarity=Rarities.RareSecret,
               regulation_mark="H")
