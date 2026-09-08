from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=209, rarity=Rarities.RareUltra,
               set_code="SWSH1", key="SWSH1",
               regulation_mark="D")
