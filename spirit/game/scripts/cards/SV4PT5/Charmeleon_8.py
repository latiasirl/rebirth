from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive

card = PokemonCardDef(
    guid="f39a25ca-45d8-433f-a404-7f9ea204af43",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon","Stage 1"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV4PT5",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    abilities=[
        Ability(
            title="Flare Veil",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
        ),
    ],
)
