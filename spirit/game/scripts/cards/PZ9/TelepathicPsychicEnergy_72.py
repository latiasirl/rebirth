from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME3/TelepathicPsychicEnergy_88.py"),
              collector_number=72, rarity=Rarities.Rare,
              set_code="PZ9", key="PZ9",
              regulation_mark="I")