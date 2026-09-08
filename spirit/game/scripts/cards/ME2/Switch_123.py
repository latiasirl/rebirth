from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../BASE1/Switch_95.py"),
               collector_number=123, rarity=Rarities.RareUltra,
               set_code="ME2", key="ME2",
               regulation_mark="I")
