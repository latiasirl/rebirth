from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=62, rarity=Rarities.RareHolo,
               set_code="SWSH35", key="SWSH35",
               regulation_mark="D")
