from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/VitalityBand_185.py"),
               collector_number=197, rarity=Rarities.Uncommon,
               set_code="SV1", key="SV1",
               regulation_mark="G")
