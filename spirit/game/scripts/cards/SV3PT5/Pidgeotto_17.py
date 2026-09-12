from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="8a21bddb-a1a5-497f-8997-6515d89e8e0a",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto","Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV3PT5",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
