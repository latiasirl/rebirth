from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../AQ/EnergySwitch_120.py"),
               collector_number=212, rarity=Rarities.RareSecret,
               set_code="SWSH12", key="SWSH12",
               regulation_mark="F")
