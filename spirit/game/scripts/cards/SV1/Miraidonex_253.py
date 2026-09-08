from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV1/Miraidonex_81.py"),
               collector_number=253, rarity=Rarities.RareSecret,
               set_code="SV1", key="SV1",
               regulation_mark="G")
