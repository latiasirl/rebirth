from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/Eri_146.py"),
               collector_number=210, rarity=Rarities.RareUltra,
               set_code="SV085", key="SV085",
               regulation_mark="H")
