from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=60, rarity=Rarities.Rare,
               set_code="SWSH45", key="SWSH45",
               regulation_mark="D")
