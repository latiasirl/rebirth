from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/ProfessorsResearch_178.py"),
               collector_number=190, rarity=Rarities.Rare,
               set_code="SV1", key="SV1",
               regulation_mark="G")
