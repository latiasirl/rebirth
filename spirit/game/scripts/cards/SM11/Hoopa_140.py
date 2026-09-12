from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, self_energy_discard_attack


def _has_ability(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(e, dict) and e.get("abilityType") in ("PokeAbility", "PokePower")
               for e in abilities)

async def mind_shock(ctx):
    """80 damage, not affected by Weakness or Resistance."""
    await ctx.deal_damage(80, apply_modifiers=False)


card = PokemonCardDef(
    guid="fc970a8c-1d29-4685-acf8-7759cff8d230",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic"],
    subtypes=["Basic"],
    collector_number=140,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=720,
    abilities=[
        Attack(
            title="Evil Admonition",
            game_text="This attack does 20 more damage for each of your opponent's Pokémon that has an Ability.",
            cost={PokemonTypes.COLORLESS: 1},
            damage_operator="+",
            effect=damage_per(count_in_play("opponent", _has_ability), 20, base=10),
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=mind_shock,
        ),
    ],
)