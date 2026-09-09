from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV09/IrissFightingSpirit_149.py"),
              collector_number=180, rarity=Rarities.RareUltra,
              set_code="SV09", key="SV09",
              regulation_mark="I")