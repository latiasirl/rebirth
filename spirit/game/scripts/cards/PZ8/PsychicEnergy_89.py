from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../Free_Energy/PsychicEnergy_5.py"),
              collector_number=89, rarity=Rarities.Rare,
              set_code="PZ8", key="PZ8")