from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f0fffcfc-1164-42fa-b7f3-0b664676e22c",
    key="PZ4",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
