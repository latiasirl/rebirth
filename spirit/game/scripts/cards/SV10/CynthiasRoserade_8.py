from spirit.game.data_utils import PokemonCardDef, Ability, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _is_cynthias(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Cynthia's ")

card = PokemonCardDef(
    guid="78496fce-3583-4b3e-9680-3e3fb17b3878",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoserade.Name",
    display_name="Cynthia's Roserade",
    searchable_by=["Cynthia's Roserade","Stage 1","CynthiasRoserade"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    family_id=315,
    abilities=[
        Ability(
            title="Cheer On to Glory",
            game_text="Attacks used by your Cynthia's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(30, attacker_pred=_is_cynthias),
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
