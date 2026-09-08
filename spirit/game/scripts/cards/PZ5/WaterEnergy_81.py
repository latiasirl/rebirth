from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4011edd1-6981-44bd-80cf-dc2b448d46c7",
    key="PZ5",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="PZ5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
