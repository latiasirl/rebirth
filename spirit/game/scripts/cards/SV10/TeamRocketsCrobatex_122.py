from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play

async def biting_spree(ctx):
    """On evolve: you may put 2 damage counters on 2 of your opponent's Pokémon"""
    if not await ctx.ask_yes_no("Put 2 damage counters on 2 of your opponent's Pokémon?"):
        return
    
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return

    picks = await ctx.choose_cards(
        candidates, min(2, len(candidates)), minimum=1,
        prompt="Choose 2 of your opponent's Pokémon",
    )

    for pokemon in picks:
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="5521336e-6985-4e80-9b32-235da3a78f02",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsCrobatex.Name",
    display_name="Team Rocket's Crobat ex",
    searchable_by=["Team Rocket's Crobat ex", "Stage 2", "TeamRocketsCrobatex"],
    subtypes=["Stage 2"],
    collector_number=122,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Biting Spree",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may choose 2 of your opponent's Pokémon and put 2 damage counters on each of them.",
            trigger=Triggers.ON_EVOLVE,
            effect=biting_spree,
        ),
        Attack(
            title="Assassin's Return",
            game_text="You may put this Pokémon into your hand. (Discard all cards attached to this Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            effect=remove_self_from_play("hand", with_attachments="discard"),
        ),
    ],
)