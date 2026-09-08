from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=150, rarity=Rarities.RareUltra,
               set_code="CZ", key="CZ",
               regulation_mark="F")
