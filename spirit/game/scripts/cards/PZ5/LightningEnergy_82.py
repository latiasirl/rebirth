from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8cf1d373-74ed-44d0-9fb4-ee19be7b1c7b",
    key="PZ5",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="PZ5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
