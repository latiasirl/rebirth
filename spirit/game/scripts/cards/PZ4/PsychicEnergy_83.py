from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="078a99bd-9716-473c-ad5a-b271aeb43851",
    key="PZ4",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
