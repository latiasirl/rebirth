from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.models.board import BoardState


def _has_fire_energy(pokemon, carrier):
    return pokemon is carrier and any(
        energy_provides_type(e, PokemonTypes.FIRE.value)
        for e in BoardState.attached_energies(pokemon)
    )

def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)

async def blazing_flight(ctx):
    """Discard 2 Fire Energy from this Pokémon, and this attack does 120 damage
    to 1 of your opponent's Pokémon."""
    await ctx.discard_energy_from(
        ctx.attacker, 2,
        predicate=_is_fire_energy,
        prompt="Choose 3 Energy to discard from this Pokémon",
    )
    await snipe_attack(120)(ctx)


card = PokemonCardDef(
    guid="bba9f044-bc93-4ba1-afb2-7c31e0110ada",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Ability(
            title="Flare Float",
            game_text="If this Pokémon has any Fire Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_has_fire_energy),
        ),
        Attack(
            title="Blazing Flight",
            game_text="Discard 2 Fire Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 3},
            effect=blazing_flight,
        ),
    ],
)