from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="214eec52-6cd7-4b64-b410-bc8754a6acab",
    key="PZ4",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
