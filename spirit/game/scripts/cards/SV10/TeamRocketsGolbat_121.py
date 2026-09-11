from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def sneaky_bite(ctx):
    """On evolve: you may put 2 damage counters on 1 of your opponent's Pokémon"""
    if not await ctx.ask_yes_no("Put 2 damage counters on 1 of your opponent's Pokémon?"):
        return
    
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon",)
    if target is None:
        return
    
    await ctx.place_damage_counters(2, [target])


card = PokemonCardDef(
    guid="50018912-8c93-44f1-903d-56f6373beb7b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    display_name="Team Rocket's Golbat",
    searchable_by=["Team Rocket's Golbat", "Stage 1", "TeamRocketsGolbat"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Sneaky Bite",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=sneaky_bite,
        ),
        Attack(
            title="Confuse Ray",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)