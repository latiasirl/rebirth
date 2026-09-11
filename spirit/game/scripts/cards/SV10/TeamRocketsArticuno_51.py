from spirit.game.data_utils import PokemonCardDef, Ability, Attack, def_for, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import attack_effect_shield_passive


def is_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's")

def repelling_veil_protects(target, carrier):
    return (
        target.owning_player_id == carrier.owning_player_id
        and is_rockets(target)
    )


card = PokemonCardDef(
    guid="2cebb9a0-6429-4b59-9623-10192415bbaf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArticuno.Name",
    display_name="Team Rocket's Articuno",
    searchable_by=["Team Rocket's Articuno","Basic","TeamRocketsArticuno"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Repelling Veil",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to your Basic Team Rocket's Pokémon. (Existing effects are not removed. Damage is not an effect.)",
            passive=attack_effect_shield_passive(repelling_veil_protects),
        ),
        Attack(
            title="Dark Frost",
            game_text="If this Pokémon has any Team Rocket's Energy attached, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
