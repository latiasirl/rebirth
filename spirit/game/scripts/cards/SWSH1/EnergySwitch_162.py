from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../AQ/EnergySwitch_120.py"),
               collector_number=162, rarity=Rarities.Uncommon,
               set_code="SWSH1", key="SWSH1",
               regulation_mark="D")
