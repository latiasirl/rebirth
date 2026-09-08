from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="3e6a8130-a34a-4c7a-b51f-47e0123143d7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    display_name="Cynthia's Roselia",
    searchable_by=["Cynthia's Roselia","Basic","CynthiasRoselia"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
