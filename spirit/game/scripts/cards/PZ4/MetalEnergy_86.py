from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="965ad5fb-e50c-405b-b062-2a5d9ac7073e",
    key="PZ4",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="PZ4",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
