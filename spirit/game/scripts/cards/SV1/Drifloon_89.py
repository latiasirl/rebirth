from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on

card = PokemonCardDef(
    guid="e8e44a0a-95f1-4b3a-bb05-bd8493b9f3fd",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=425,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
        Attack(
            title="Balloon Blast",
            game_text="This attack does 30 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 30),
        ),
    ],
)
