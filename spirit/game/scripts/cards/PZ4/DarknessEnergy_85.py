from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="171e849b-1d19-497d-aa90-4abc702b5ccd",
    key="PZ4",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False
)
