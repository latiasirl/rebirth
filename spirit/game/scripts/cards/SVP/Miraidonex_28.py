from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV1/Miraidonex_81.py"),
               collector_number=28, rarity=Rarities.RarePromo,
               set_code="SVP", key="SVP",
               regulation_mark="G")
