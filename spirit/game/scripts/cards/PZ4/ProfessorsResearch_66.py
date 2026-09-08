from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=66, rarity=Rarities.Rare,
               set_code="PZ4", key="PZ4",
               regulation_mark="G")
