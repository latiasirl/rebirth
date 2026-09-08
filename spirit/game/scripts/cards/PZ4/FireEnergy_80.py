from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="208f3f4d-2a0e-4f7a-8862-f7618daf53af",
    key="PZ4",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIRE,
    is_special=False
)
